# API_DOCS.md

## API 參考文件

### 基礎 URL
```
http://localhost:8000
```

### 1. 根端點 (GET /)

**用途**: 獲取服務基本資訊

**請求**:
```bash
GET /
```

**回應**:
```json
{
  "message": "MNIST Multi-Model Inference API",
  "models": ["SimpleNN", "SimpleCNN", "ViT_Custom", ...]
}
```

**欄位說明**:
- `message`: 服務描述
- `models`: 已載入的模型列表

---

### 2. 健康檢查 (GET /health)

**用途**: 檢查服務健康狀態

**請求**:
```bash
GET /health
```

**回應**:
```json
{
  "status": "healthy",
  "device": "cuda",
  "models_count": 7
}
```

**欄位說明**:
- `status`: 服務狀態 (healthy/unhealthy)
- `device`: 運算設備 (cuda/cpu)
- `models_count`: 已載入模型數量

---

### 3. 模型列表 (GET /models)

**用途**: 獲取可用模型名稱列表

**請求**:
```bash
GET /models
```

**回應**:
```json
{
  "models": ["SimpleNN", "SimpleCNN", "ViT_Custom", ...]
}
```

---

### 4. 推論端點 (POST /predict)

**用途**: 上傳圖片進行多模型推論

**請求**:
```bash
POST /predict
Content-Type: multipart/form-data
```

**參數**:
- `file`: 圖片檔案 (JPEG/PNG/BMP)

**curl 範例**:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -F "file=@digit_7.png"
```

**Python 範例**:
```python
import requests

url = "http://localhost:8000/predict"
with open("test.png", "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print(response.json())
```

**成功回應** (HTTP 200):
```json
{
  "success": true,
  "results": {
    "SimpleNN": {
      "model_name": "SimpleNN",
      "prediction": 7,
      "confidence": 0.923,
      "probabilities": [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.923, 0.031, 0.018]
    },
    "SimpleCNN": {
      "model_name": "SimpleCNN",
      "prediction": 7,
      "confidence": 0.978,
      "probabilities": [0.001, 0.001, 0.002, 0.002, 0.003, 0.003, 0.004, 0.978, 0.003, 0.003]
    }
  },
  "best_model": "SimpleCNN",
  "best_prediction": 7
}
```

**欄位說明**:

#### InferenceResponse (最外層)
- `success`: 是否成功
- `results`: 各模型推論結果字典
- `best_model`: 信心度最高的模型名稱
- `best_prediction`: 最佳預測數字

#### PredictionResult (單一模型)
- `model_name`: 模型名稱
- `prediction`: 預測數字 (0-9)
- `confidence`: 信心度 (0-1)
- `probabilities`: 10 個數字的概率分布

**錯誤回應**:

1. 無模型載入:
```json
{
  "detail": "No models loaded"
}
```
狀態碼: 503

2. 無效圖片:
```json
{
  "detail": "Invalid image: cannot identify image file"
}
```
狀態碼: 400

---

## 圖片要求

### 支援格式
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)

### 建議規格
- **大小**: 任意 (會自動調整為 28×28)
- **色彩**: 彩色或灰階皆可
- **背景**: 建議白色背景，黑色數字
- **對比**: 高對比度效果最佳

### 預處理效果
原始圖片會經過以下處理：
1. 轉為灰階
2. 高斯模糊去噪
3. 二值化 (Otsu)
4. 數字區域裁剪
5. 調整為 28×28
6. 置中對齊

---

## 狀態碼參考

| 狀態碼 | 意義 | 常見情況 |
|--------|------|----------|
| 200 | 成功 | 推論完成 |
| 400 | 錯誤請求 | 圖片格式無效 |
| 503 | 服務不可用 | 無模型載入 |
| 500 | 伺服器錯誤 | 內部處理錯誤 |

---

## 效能提示

1. **圖片大小**: 保持圖片在 1MB 以內
2. **併發請求**: 服務支持非同步處理，可同時處理多個請求
3. **GPU 加速**: 如有 CUDA 設備，會自動啟用 GPU 加速
4. **快取考慮**: 相同圖片多次請求會重新計算，可考慮客戶端快取
