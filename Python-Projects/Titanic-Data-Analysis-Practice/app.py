"""
Titanic 數據分析主程序
包含數據生成、清洗和特徵工程功能
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

def generate_titanic_data():
    """生成模擬的 Titanic 數據集"""
    np.random.seed(42)
    n = 891
    
    df = pd.DataFrame({
        'PassengerId': range(1, n+1),
        'Survived': np.random.choice([0,1], n, p=[0.62, 0.38]),
        'Pclass': np.random.choice([1,2,3], n, p=[0.24,0.21,0.55]),
        'Name': [f'Passenger_{i}' for i in range(1, n+1)],
        'Sex': np.random.choice(['male','female'], n, p=[0.65, 0.35]),
        'Age': np.random.randint(1, 80, n).astype(float),
        'SibSp': np.random.choice([0, 1, 2, 3, 4], n, p=[0.68, 0.23, 0.06, 0.02, 0.01]),
        'Parch': np.random.choice([0, 1, 2, 3], n, p=[0.76, 0.13, 0.08, 0.03]),
        'Ticket': [f'TICKET{i:04d}' for i in range(1, n + 1)],
        'Fare': np.random.gamma(2, 15, n),
        'Cabin': [f'C{np.random.randint(1,100)}' if np.random.random() > 0.77 else None for _ in range(n)],
        'Embarked': np.random.choice(['S', 'C', 'Q'], n, p=[0.72, 0.19, 0.09])
    })
    
    return df

def clean_data(df):
    """數據清洗和預處理"""
    df_clean = df.copy()
    
    # 刪除 Cabin 欄位（缺失率過高）
    if 'Cabin' in df_clean.columns:
        df_clean = df_clean.drop('Cabin', axis=1)
    
    # 處理缺失值
    if 'Age' in df_clean.columns:
        age_median = df_clean['Age'].median()
        df_clean['Age'] = df_clean['Age'].fillna(age_median)
    
    if 'Embarked' in df_clean.columns:
        embarked_mode = df_clean['Embarked'].mode()[0]
        df_clean['Embarked'] = df_clean['Embarked'].fillna(embarked_mode)
    
    # 刪除重複值
    df_clean = df_clean.drop_duplicates()
    
    return df_clean

def feature_engineering(df):
    """特徵工程"""
    df_features = df.copy()
    
    # 1. 創建 FamilySize
    df_features['FamilySize'] = df_features['SibSp'] + df_features['Parch'] + 1
    
    # 2. 創建 IsAlone
    df_features['IsAlone'] = (df_features['FamilySize'] == 1).astype(int)
    
    # 3. 年齡分組
    def categorize_age(age):
        if age < 18:
            return '兒童'
        elif age < 30:
            return '青少年'
        elif age < 60:
            return '成年人'
        else:
            return '老人'
    
    df_features['AgeGroup'] = df_features['Age'].apply(categorize_age)
    
    # 4. 性別編碼
    df_features['Sex_Encoded'] = df_features['Sex'].map({'male': 0, 'female': 1})
    
    # 5. Embarked One-Hot 編碼
    embarked_dummies = pd.get_dummies(df_features['Embarked'], prefix='Embarked')
    df_features = pd.concat([df_features, embarked_dummies], axis=1)
    
    return df_features

def main():
    """主函數：執行完整流程"""
    print("開始 Titanic 數據分析...")
    
    # 生成數據
    df = generate_titanic_data()
    print(f"✅ 生成模擬數據，形狀: {df.shape}")
    
    # 保存原始數據
    df.to_csv('data/raw_titanic.csv', index=False)
    print("✅ 原始數據已保存: data/raw_titanic.csv")
    
    # 清洗數據
    df_clean = clean_data(df)
    print(f"✅ 數據清洗完成，形狀: {df_clean.shape}")
    
    # 特徵工程
    df_final = feature_engineering(df_clean)
    print(f"✅ 特徵工程完成，形狀: {df_final.shape}")
    
    # 保存清洗後數據
    df_final.to_csv('data/cleaned_titanic.csv', index=False)
    print("✅ 清洗後數據已保存: data/cleaned_titanic.csv")
    
    print("🎉 數據處理完成！")

if __name__ == "__main__":
    main()
