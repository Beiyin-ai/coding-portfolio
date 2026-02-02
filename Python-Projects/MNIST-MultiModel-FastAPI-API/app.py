import os
import io
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
import cv2
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
from torchvision import transforms
from transformers import ViTForImageClassification, ViTImageProcessor, pipeline
from pathlib import Path

# 定義模型架構
# 1. class SimpleNN
# 2. class SimpleCNN
# 3.自建的ViT
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 128), nn.ReLU(),
            nn.Linear(128, 64), nn.ReLU(),
            nn.Linear(64, 10)
        )
    def forward(self, x):
        return self.model(x)


class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1), nn.ReLU(), nn.MaxPool2d(2)
        )
        self.fc_layers = nn.Sequential(nn.Linear(64*7*7, 128), nn.ReLU(), nn.Linear(128, 10))

    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1)
        return self.fc_layers(x)
    

class PatchEmbedding(nn.Module):
    def __init__(self, img_size=28, patch_size=7, in_chans=1, embed_dim=64):
        super().__init__()
        self.n_patches = (img_size // patch_size) ** 2
        self.proj = nn.Conv2d(in_chans, embed_dim, kernel_size=patch_size, stride=patch_size)

    def forward(self, x):
        return self.proj(x).flatten(2).transpose(1,2)
    
class TransformerEncoderBlock(nn.Module):
    def __init__(self, dim, num_heads, mlp_ratio=4.0, dropout=0.1):
        super().__init__()
        # 正規化
        self.norm1 = nn.LayerNorm(dim)
        # self-attention
        self.attn = nn.MultiheadAttention(dim, num_heads, dropout=dropout, batch_first=True)
        # 正規化
        self.norm2 = nn.LayerNorm(dim)
        self.mlp = nn.Sequential(
            nn.Linear(dim, int(dim*mlp_ratio)), nn.GELU(), nn.Dropout(dropout),
            nn.Linear(int(dim * mlp_ratio), dim), nn.Dropout(dropout)
        )
    
    def forward(self, x):
        # attention回傳:1.計算結果, 2.權重
        attn_out, _ = self.attn(self.norm1(x), self.norm1(x), self.norm1(x))
        # 殘差連結
        x = x + attn_out
        return x + self.mlp(self.norm2(x))
    

class ViT_MNIST(nn.Module):
    def __init__(self, img_size=28, patch_size=7, in_chans=1, num_classes=10, embed_dim=64, depth=6, num_heads=4, dropout=0.1):
        super().__init__()
        # step1: embedding
        self.patch_embed = PatchEmbedding(img_size, patch_size, in_chans, embed_dim)
        # step2: cls_token
        self.cls_token = nn.Parameter(torch.zeros(1,1, embed_dim))
        # step3: position info
        self.pos_embed = nn.Parameter(torch.zeros(1, 1+self.patch_embed.n_patches, embed_dim))
        # step4: transformer
        self.blocks = nn.ModuleList([
            TransformerEncoderBlock(embed_dim, num_heads, dropout=dropout) for _ in range(depth)
        ])
        # step5: 正規化
        self.norm = nn.LayerNorm(embed_dim)
        # step6: 輸出10個類別
        self.head = nn.Linear(embed_dim, num_classes)

        # cls token & position
        nn.init.trunc_normal_(self.pos_embed, std=0.02)
        nn.init.trunc_normal_(self.cls_token, std=0.02)

    def forward(self, x):
        B = x.size(0)
        x = self.patch_embed(x)
        x = torch.cat((self.cls_token.expand(B, -1, -1), x), dim=1) + self.pos_embed

        for blk in self.blocks:
            x = blk(x)

        return self.head(self.norm(x)[:, 0])
    


# FastAPI : python web-server
app = FastAPI(title="MNIST Multi-Model Inference API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 參數設定
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
models = {}
vit_processor = None
MODeL_DIR = os.environ.get("MODEL_DIR", "/app/models")

# 資料預處理
def preprocess_for_mnist(pil_img):
    gray = np.array(pil_img.convert('L'))
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
        digit = thresh[y:y+h, x:x+w]
        size = 20
        digit = cv2.resize(digit, (size, int(h*size/w)) if w > h else (int(w*size/h), size))
        canvas = np.zeros((28, 28), dtype=np.uint8)
        new_h, new_w = digit.shape
        canvas[(28-new_h)//2:(28-new_h)//2+new_h, (28-new_w)//2:(28-new_w)//2+new_w] = digit
        return Image.fromarray(canvas)
    return Image.fromarray(thresh).resize((28, 28))


@app.on_event("startup")
async def load_model():
    global models, vit_processor
    print(f"Loading models from {MODeL_DIR} on {device}")

    # 自定義模型*3
    model_configs=[
        ("simple_nn_mnist.pth", "SimpleNN", SimpleNN),
        ("simple_cnn_mnist.pth", "SimpleCNN", SimpleCNN),
        ("myvit_mnist.pth", "ViT_Custom", ViT_MNIST),
    ]

    for fname, name, cls in model_configs:
        path = Path(MODeL_DIR) / fname
        if path.exists():
            model = cls().to(device)
            model.load_state_dict(torch.load(path, map_location=device))
            model.eval()
            models[name] = {"type": "mnist", "model": model}
            print(f"Loaded: {name}")

    # HF + pretrained
    hf_pth_configs=[
        ("myvit_mnist_hf_4060.pth", "ViT_HF_4060"),
        ("myvit_mnist_hf_best_tuned.pth", "ViT_HF_BestTuned"),
    ]

    for fname, name in hf_pth_configs:
        path = Path(MODeL_DIR) / fname
        if path.exists():
            try:
                if vit_processor is None:
                    vit_processor = ViTImageProcessor.from_pretrained("google/vit-base-patch16-224")

                model = ViTForImageClassification.from_pretrained(
                    "google/vit-base-patch16-224", num_labels=10, ignore_mismatched_sizes=True
                ).to(device)

                model.load_state_dict(torch.load(path, map_location=device))
                model.eval()
                models[name] = {"type": "hf_vit", "model": model, "processor": vit_processor}
                print(f"Loaded: {name}")
            except Exception as e:
                print(f"Failed loading...{name}: {e}")

    # HF + 別人訓練好的 + ImageNet
    try:
        pipe = pipeline(
            "image-classification",
            model = "google/vit-base-patch16-224",
            device=0 if torch.cuda.is_available() else -1
        )

        models["ViT_ImageNet"] = {"type": "pipeline", "model": pipe}
        print(f"Loaded: ViT_ImageNet(google/vit-base-patch16-224)")
    except Exception as e:
                print(f"Failed loading ViT_ImageNet: {e}")

    # HF + 別人訓練好的 + MNIST
    try:
        v_3rd_proc = ViTImageProcessor.from_pretrained("farleyknight-org-username/vit-base-mnist")
        v_3rd_model = ViTForImageClassification.from_pretrained(
                    "farleyknight-org-username/vit-base-mnist"
                ).to(device)           
        v_3rd_model.eval()
        models["ViT_3rd_MNIST"] = {"type": "hf_vit", "model": v_3rd_model, "processor": v_3rd_proc}
        print(f"Loaded: ViT_3rd_MNIST(farleyknight-org-username/vit-base-mnist)")
    except Exception as e:
        print(f"Failed loading ViT_3rd_MNIST: {e}")      

    print(f"Total: {len(models)} models loaded")


# 定義回應訊息
class PredictionResult(BaseModel):
    model_name: str
    prediction: int
    confedence: float
    probabilities: list[float]

class InferenceResponse(BaseModel):
    success: bool
    results: Dict[str, PredictionResult]
    best_model: str
    best_prediction: int



# 定義服務的API: router
@app.get("/")
async def root():
    return {"message": "MNIST Multi-Model Ineference API", "models": list(models.keys())}

@app.get("/health")
async def health():
    return {"status": "healthy", "device": str(device), "models_count": len(models)}

@app.get("/models")
async def list_models():
    return {"models": list(models.keys())}


@app.post("/predict", response_model=InferenceResponse)
async def predict(file: UploadFile = File(...)):
    if not models:
        raise HTTPException(status_code=503, detail="No models loaded")
    
    # 將上船的圖片改成RGB
    try:
        pil_img = Image.open(io.BytesIO(await file.read())).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalide image:{e}")

    # 資料預處理
    processed = preprocess_for_mnist(pil_img)

    t28 = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5))])(processed).unsqueeze(0).to(device)
    results = {}

    best_conf, best_model, best_pred = 0, "", -1

    # 推論
    with torch.no_grad():
        for name, info in models.items():
            if info["type"] == "mnist":
                logits = info["model"](t28)

                # 轉機率
                probs= torch.softmax(logits, dim=1)[0].cpu().numpy()
            elif info["type"] == "pipeline":
                pipe_results = info["model"](pil_img, top_k=10)
                probs = np.zeros(10)

                for r in pipe_results:
                    label = r["label"]
                    try:
                        idex = int(label.split("_")[-1]) if "_" in label else int(label)

                        if 0 <= idex <10:
                            probs[idex] = r["score"]

                    except:
                        pass

            else: # hf+mnist
                input = info["processor"](images=pil_img, return_tensors= "pt")
                input = {k: v.to(device) for k, v in input.items()}
                outputs = info["model"](**input)
                probs = torch.softmax(outputs.logits, dim=1)[0].cpu().numpy()

            # 預測值
            pred = int(np.argmax(probs))

            # 信心度
            conf = float(np.max(probs))

            results[name] = PredictionResult(
                model_name=name,
                prediction=pred,
                confedence=conf,
                probabilities=probs.tolist()
            )

            if conf > best_conf:
                best_conf = conf
                best_model = name
                best_pred = pred

    return InferenceResponse(
        success=True,
        results=results,
        best_model=best_model,
        best_prediction=best_pred
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)