# Titanic 數據分析練習

## 專案概述
本專案對 Titanic 數據集進行完整的數據分析流程練習，包括：
1. 數據讀取與探索性分析
2. 數據清洗與預處理
3. 特徵工程
4. PCA 主成分分析
5. 數據可視化

## 文件結構
- `titanic.py` - 數據讀取與探索（需先運行 app.py）
- `app.py` - 產生模擬數據、數據清洗與特徵工程（主要文件）
- `pca.py` - PCA 分析（需先運行 app.py）
- `requirements.txt` - 依賴套件列表
- `data/` - 數據文件目錄（由 app.py 自動生成）

## 使用方式
```bash
# 安裝依賴
pip install -r requirements.txt

# 執行流程（按順序）
python app.py     # 1. 產生模擬數據、清洗數據、特徵工程
python titanic.py # 2. 數據探索分析（可選）
python pca.py     # 3. PCA 分析
```

## 執行結果
運行後會產生：
1. `data/titanic.csv` - 模擬的原始數據
2. `data/cleaned_titanic.csv` - 清洗後的數據
3. `missing_values.png` - 缺失值可視化圖表
4. `pca_analysis.png` - PCA 分析圖表
5. `pca_results.csv` - PCA 結果數據

## 注意事項
- 請按順序執行：`app.py` → `pca.py`
- `titanic.py` 僅用於數據探索，需要在 `app.py` 之後運行
- 確保 matplotlib 支持中文字體顯示
