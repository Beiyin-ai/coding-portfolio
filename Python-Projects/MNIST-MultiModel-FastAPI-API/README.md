# MNIST 多模型推論 FastAPI API

這是一個用於手寫數字辨識（MNIST）的多模型推論 API 服務，使用 FastAPI 框架構建。支持多種深度學習模型同時推論，並提供統一的 API 接口。

## ✨ 功能特色

- **多模型支持**：同時載入並運行多種不同架構的模型
- **即時推論**：接受圖片上傳並返回多模型推論結果
- **最佳模型選擇**：自動選擇信心度最高的模型結果
- **健康監控**：提供服務健康狀態檢查端點
- **CORS 支持**：跨域請求支援，方便前端整合

## 🤖 支持的模型類型

1. **自定義模型**（基於 PyTorch）
   - SimpleNN：簡單全連接神經網路
   - SimpleCNN：卷積神經網路
   - ViT_Custom：自定義 Vision Transformer

2. **HuggingFace 模型**（基於 transformers）
   - ViT_HF_4060：基於 ViT 的微調模型
   - ViT_HF_BestTuned：最佳微調版本
   - ViT_ImageNet：預訓練 ImageNet 模型
   - ViT_3rd_MNIST：第三方預訓練 MNIST 模型

## 🚀 快速開始

### 環境設置

```bash
# 複製專案
git clone <your-repo-url>
cd MNIST-MultiModel-FastAPI-API

# 安裝依賴
pip install -r requirements.txt

# 設定模型路徑（可選）
export MODEL_DIR="./models"
```

### 模型檔案下載

由於模型檔案較大，請從以下連結下載並放置於 `models/` 目錄：
- [模型檔案下載連結](你的下載連結)

或使用以下指令準備模型檔案：

```bash
# 建立 models 目錄
mkdir -p models

# 將你的 .pth 模型檔案複製到此目錄
# cp /path/to/your/models/*.pth models/
```

### 啟動服務

```bash
python app.py
```

服務將在 `http://localhost:8000` 啟動。

## 📡 API 端點

### 1. 根目錄 - 服務資訊
```
GET /
```
返回 API 基本資訊和已載入模型清單。

### 2. 健康檢查
```
GET /health
```
檢查服務狀態、設備資訊和模型數量。

### 3. 模型清單
```
GET /models
```
返回所有可用模型的名稱。

### 4. 推論端點
```
POST /predict
Content-Type: multipart/form-data
```
上傳圖片進行推論。

**請求範例（curl）:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -F "file=@test_image.png"
```

**回應格式:**
```json
{
  "success": true,
  "results": {
    "SimpleNN": {
      "model_name": "SimpleNN",
      "prediction": 7,
      "confidence": 0.95,
      "probabilities": [0.01, 0.02, ..., 0.95]
    }
  },
  "best_model": "SimpleNN",
  "best_prediction": 7
}
```

## 🏗️ 專案架構

```
app.py                    # 主應用程式
├── 模型定義
│   ├── SimpleNN          # 簡單神經網路
│   ├── SimpleCNN         # 卷積神經網路
│   └── ViT_MNIST         # Vision Transformer
├── FastAPI 應用
│   ├── 啟動事件         # 模型載入
│   ├── CORS 設定        # 跨域支援
│   └── API 端點         # RESTful 接口
└── 資料預處理
    └── MNIST 專用處理    # 影像正規化
```

## 🔧 技術棧

- **後端框架**: FastAPI (非同步支持)
- **深度學習**: PyTorch, HuggingFace Transformers
- **影像處理**: OpenCV, Pillow
- **API 文件**: 自動生成 Swagger UI

## 📊 模型效能比較

| 模型 | 準確率 | 推論速度 | 特點 |
|------|--------|----------|------|
| SimpleNN | ~95% | 最快 | 輕量級，適合快速推論 |
| SimpleCNN | ~98% | 快速 | 平衡效能與速度 |
| ViT_Custom | ~99% | 中等 | 最高準確率 |
| ViT_HF | ~99.2% | 較慢 | 預訓練優勢 |

## 📁 目錄結構

```
MNIST-MultiModel-FastAPI-API/
├── app.py              # 主程式
├── requirements.txt    # 依賴套件
├── README.md          # 中文說明
├── README.en.md       # 英文說明
├── docs/              # 說明文件
│   ├── ARCHITECTURE.md
│   └── API_DOCS.md
└── models/            # 模型權重檔案
    ├── README.md
    └── *.pth
```

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📄 授權

MIT License
