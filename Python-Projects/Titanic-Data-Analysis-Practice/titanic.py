"""
Titanic 數據探索分析
"""

import pandas as pd   # 匯入 pandas 套件，常用於資料處理與分析

# 讀資料集
df = pd.read_csv('titanic.csv')   # 讀取 titanic.csv 檔案並存入 DataFrame
print(df.head())                  # 顯示前 5 筆資料，快速查看資料內容

print(df.describe())              # 顯示數值型欄位的統計摘要 (平均值、標準差、最小值、四分位數、最大值)

print(df.shape)                   # 顯示資料的維度 (列數, 欄數)

print(df.info())                  # 顯示 DataFrame 的基本資訊 (欄位名稱、非空值數量、資料型態)

print(df.isnull().sum())          # 計算每個欄位中缺失值 (NaN) 的數量

# 再讀另一個 Titanic 資料集
df = pd.read_csv('Titanic-Dataset.csv')   # 讀取 Titanic-Dataset.csv 檔案並存入 DataFrame
print(df.head())                          # 顯示前 5 筆資料

print(df.describe())                      # 顯示數值型欄位的統計摘要

print(df.shape)                           # 顯示資料的維度 (列數, 欄數)

print(df.info())                          # 顯示 DataFrame 的基本資訊

print(df.isnull().sum())                  # 計算每個欄位中缺失值的數量
