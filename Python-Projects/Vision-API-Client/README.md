# Vision API Client

本機端 Vision API 客戶端，用於圖片分析和理解。

## ✨ 功能特色

- 🖼️ **圖片分析**：支援 PNG、JPG 格式
- 🔍 **物件偵測**：識別圖片中的人物、物品
- 👥 **人數計算**：自動統計圖片中的人數
- 🎯 **可疑行為偵測**：監視器畫面分析
- 📊 **GPU 監控**：即時顯示顯示卡使用狀況

## 📁 專案結構

```
Vision-API-Client/
├── README.md          # 專案說明
├── requirements.txt   # 依賴套件
├── .gitignore        # Git 忽略規則
├── img2txt_p1.py     # Python 版 Vision API
├── img2txt_p2.sh     # Shell 版 Vision API
├── watch-nvidia.sh   # GPU 監控工具
└── examples/         # 範例圖片
    └── test_images/  # 測試用圖片
```

## 🚀 安裝方式

```bash
# 安裝依賴套件
pip install -r requirements.txt

# 給予執行權限（Shell 腳本）
chmod +x img2txt_p2.sh watch-nvidia.sh
```

## 📝 使用方法

### Python 版本
```bash
python img2txt_p1.py
```

### Shell 版本
```bash
./img2txt_p2.sh p1.png
```

### GPU 監控
```bash
./watch-nvidia.sh
```

## 🔧 設定說明

本專案需要連接到本地 Vision Model 服務（預設位址：http://localhost:8880/v1）

## 📸 範例圖片

測試圖片放在 `examples/test_images/` 目錄下：
- p1.png：監視器畫面
- p2.png：街景多人
- p3.png：一般場景

## 📝 授權條款

MIT License
