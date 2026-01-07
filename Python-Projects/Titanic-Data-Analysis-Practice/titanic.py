"""
Titanic 數據探索分析
"""

import pandas as pd

def explore_data():
    """探索數據"""
    print("Titanic 數據探索分析")
    print("=" * 60)
    
    try:
        # 讀取原始數據
        df_raw = pd.read_csv('data/raw_titanic.csv')
        print(f"\n📊 原始數據集")
        print(f"📁 文件路徑: data/raw_titanic.csv")
        print(f"📐 數據形狀: {df_raw.shape} (行數 × 列數)")
        print(f"\n🔍 前3行數據:")
        print(df_raw.head(3))
        
    except FileNotFoundError:
        print("⚠️  未找到原始數據文件，請先運行 app.py")
    
    print("-" * 45)
    
    try:
        # 讀取清洗後數據
        df_clean = pd.read_csv('data/cleaned_titanic.csv')
        print(f"\n📊 清洗後數據集")
        print(f"📁 文件路徑: data/cleaned_titanic.csv")
        print(f"📐 數據形狀: {df_clean.shape} (行數 × 列數)")
        print(f"\n🔍 前3行數據:")
        print(df_clean.head(3))
        
    except FileNotFoundError:
        print("⚠️  未找到清洗後數據文件，請先運行 app.py")
    
    print("=" * 60)
    print("✅ 數據探索完成！")

if __name__ == "__main__":
    explore_data()
