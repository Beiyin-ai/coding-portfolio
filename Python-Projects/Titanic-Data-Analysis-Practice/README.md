# Titanic 數據分析練習

## 📊 專案概述
本專案對 Titanic 數據集進行完整的數據分析流程練習，展示從原始數據到特徵工程的完整數據科學工作流。

## 🎯 專案目標
- 掌握完整的數據分析流程
- 實踐數據清洗和預處理技巧
- 學習特徵工程方法
- 理解 PCA 降維技術

## 📁 文件結構
Titanic-Data-Analysis-Practice/
├── README.md # 專案說明
├── requirements.txt # 依賴套件列表
├── .gitignore # Git 忽略文件
├── app.py # 主程序：數據生成、清洗、特徵工程
├── titanic.py # 數據探索性分析
├── pca.py # PCA 主成分分析
├── data/ # 數據文件目錄
│ ├── raw_titanic.csv # 原始模擬數據
│ └── cleaned_titanic.csv # 清洗後數據
└── results/ # 輸出結果目錄（運行後生成）

text

## 🚀 快速開始

### 1. 安裝依賴
```bash
pip install -r requirements.txt
2. 運行順序
bash
# 第一步：生成和清洗數據
python app.py

# 第二步：數據探索
python titanic.py

# 第三步：PCA分析
python pca.py
3. 檢查專案
bash
# 查看文件結構
ls -la
ls -la data/
🔧 功能說明
app.py
生成模擬 Titanic 數據集

數據清洗（處理缺失值、刪除無效列）

特徵工程（創建新特徵、編碼轉換）

titanic.py
數據探索性分析

統計信息展示

缺失值分析

pca.py
主成分分析

特徵降維

可視化結果

📈 輸出示例
運行 app.py 後會輸出：

text
✅ 數據清洗和特徵工程完成！
原始數據: (891, 12)
清洗後數據: (891, 18)
新增特徵: ['FamilySize', 'IsAlone', 'AgeGroup', 'Sex_Encoded', ...]
📝 注意事項
請按順序執行：app.py → pca.py

使用隨機種子 42 確保結果可重現

如需圖片輸出，取消註釋 app.py 和 pca.py 中的保存代碼

📄 許可證
僅供學習使用

## 🔧 代碼結構說明

### app.py
主要功能函數：
- `generate_titanic_data()`: 生成模擬 Titanic 數據
- `clean_data(df)`: 數據清洗和預處理
- `feature_engineering(df)`: 特徵工程
- `main()`: 主函數（可選執行）

使用方式：
```python
# 單獨使用某個功能
from app import generate_titanic_data, clean_data, feature_engineering

# 生成數據
df = generate_titanic_data()

# 清洗數據
df_clean = clean_data(df)

# 特徵工程
df_final = feature_engineering(df_clean)

# 或者直接運行主程序
python app.py
titanic.py
數據探索功能：

explore_data(): 探索原始和清洗後數據

使用方式：

python
from titanic import explore_data

# 執行數據探索
explore_data()
pca.py
PCA 分析功能：

perform_pca_analysis(): 執行主成分分析

使用方式：

python
from pca import perform_pca_analysis

# 執行 PCA 分析
perform_pca_analysis()
⚠️ 注意事項
數據文件（CSV）和圖片文件（PNG）會被 .gitignore 忽略

運行 python app.py 會生成數據文件到 data/ 目錄

如需圖片輸出，取消註釋 app.py 和 pca.py 中的相關代碼

所有模塊都可以單獨導入和使用
