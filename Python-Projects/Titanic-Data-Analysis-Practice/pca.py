"""
PCA 主成分分析
用於 Titanic 數據的降維分析
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def perform_pca_analysis():
    """執行 PCA 分析"""
    print("開始 PCA 分析...")
    
    try:
        # 讀取數據
        df = pd.read_csv('data/cleaned_titanic.csv')
        print(f"成功讀取 cleaned_titanic.csv，形狀: {df.shape}")
        
        # 選擇數值特徵
        numerical_features = ['Age', 'Fare', 'FamilySize', 'Sex_Encoded', 'Pclass']
        
        # 檢查特徵是否存在
        available_features = [f for f in numerical_features if f in df.columns]
        print(f"可用數值特徵: {available_features}")
        
        if len(available_features) < 2:
            print("⚠️  數值特徵不足，無法進行 PCA")
            return
        
        # 提取特徵數據
        X = df[available_features].values
        
        # 標準化
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # PCA
        pca = PCA()
        X_pca = pca.fit_transform(X_scaled)
        
        # 輸出結果
        print(f"\n原始特徵數量: {len(available_features)}")
        print(f"PCA 後保留的特徵數量: {X_pca.shape[1]}")
        
        print("\n各主成分解釋的變異比例:")
        for i, ratio in enumerate(pca.explained_variance_ratio_, 1):
            print(f"  主成分 {i}: {ratio:.3f}")
        
        cumulative_ratio = np.cumsum(pca.explained_variance_ratio_)[-1]
        print(f"累積解釋變異比例: {cumulative_ratio:.3f}")
        
        print("\n✅ PCA 分析完成！")
        
    except FileNotFoundError:
        print("❌ 未找到 cleaned_titanic.csv，請先運行 app.py")
    except Exception as e:
        print(f"❌ PCA 分析失敗: {e}")

if __name__ == "__main__":
    perform_pca_analysis()
