# ARCHITECTURE.md

## 系統架構概述

本專案採用微服務架構，將多個 MNIST 手寫數字辨識模型封裝成統一的 RESTful API 服務。

## 核心組件

### 1. 模型層 (Model Layer)

#### 自定義模型
- **SimpleNN**: 三層全連接神經網路
  - 輸入: 28×28 = 784 維
  - 隱藏層: 128 → 64 神經元
  - 輸出: 10 類 (0-9)

- **SimpleCNN**: 卷積神經網路
  - 卷積層: 1→32→64 通道
  - 池化層: 2×2 MaxPooling
  - 全連接層: 64×7×7 → 128 → 10

- **ViT_MNIST**: Vision Transformer
  - Patch Embedding: 7×7 patches → 64 維
  - Transformer Encoder: 6 層, 4 頭注意力
  - CLS Token: 用於分類輸出

#### HuggingFace 模型
- **ViT_HF_4060**: 基於 google/vit-base-patch16-224 微調
- **ViT_ImageNet**: 預訓練 ImageNet 模型
- **ViT_3rd_MNIST**: 第三方預訓練 MNIST 模型

### 2. API 層 (API Layer)

#### FastAPI 應用
- **非同步處理**: 使用 async/await 提升併發能力
- **自動文檔**: Swagger UI 自動生成
- **CORS 支持**: 跨域請求處理
- **錯誤處理**: HTTP 異常狀態碼返回

#### API 端點設計
```
GET  /           # 服務資訊
GET  /health     # 健康檢查
GET  /models     # 模型列表
POST /predict    # 推論端點
```

### 3. 預處理層 (Preprocessing Layer)

#### MNIST 專用處理
1. **色彩轉換**: RGB → 灰階
2. **去噪處理**: 高斯模糊
3. **二值化**: Otsu 閾值處理
4. **邊緣檢測**: 輪廓提取
5. **正規化**: 大小調整 (28×28)
6. **標準化**: 像素值 [-1, 1]

#### 模型特定處理
- **CNN/NN**: 灰階 + 標準化
- **ViT**: RGB + HuggingFace Processor

## 資料流

```
使用者請求
    ↓
[FastAPI 接收]
    ↓
圖片預處理 (preprocess_for_mnist)
    ↓
模型推論 (多模型並行)
    ├── SimpleNN
    ├── SimpleCNN
    ├── ViT_Custom
    ├── ViT_HF
    └── ViT_ImageNet
    ↓
結果整合
    ↓
最佳模型選擇
    ↓
JSON 回應
```

## 啟動流程

```
1. FastAPI 應用初始化
2. 設定 CORS 中間件
3. 載入環境變數
4. 啟動事件: load_model()
   ├── 載入自定義模型 (.pth)
   ├── 載入 HuggingFace 模型
   └── 初始化預處理器
5. 啟動 HTTP 伺服器
```

## 配置管理

### 環境變數
- `MODEL_DIR`: 模型檔案路徑
- (隱含) `device`: CPU/CUDA 自動檢測

### 模型配置
在 `model_configs` 陣列中定義：
```python
("檔案名.pth", "顯示名稱", 模型類別)
```

## 擴展性設計

### 新增模型
1. 定義模型類別 (繼承 nn.Module)
2. 加入 model_configs
3. 在推論邏輯中處理新類型

### 新增預處理
1. 在 `preprocess_for_mnist` 中擴展
2. 或新增專用預處理函數

### 新增 API 端點
1. 使用 FastAPI 裝飾器
2. 定義 Pydantic 模型進行驗證
