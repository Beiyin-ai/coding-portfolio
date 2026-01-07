# 產生titanic資料集
import numpy as np
import pandas as pd
import matplotlib
import matplotlib
matplotlib.rcParams["font.sans-serif"] = ["DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False
matplotlib.rcParams['font.sans-serif'] = ['DejaVu Sans']  # 使用系統默認字體
matplotlib.rcParams['axes.unicode_minus'] = False

# 設定隨機種子: 確保每次產生的隨機數是一樣的
np.random.seed(42)

# 設定紀錄數量: titanic 原始收集的數量
n = 891

# 產生模擬的titanic 數據集
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

print('產生的模擬資料集:')
print(df.head())

# 將資料保存為 CSV 文件
df.to_csv('titanic.csv', index=False)
print('資料已保存為 titanic.csv')

# Age, Embarked, Cabin: 有缺失值
# 隨機寫入缺失值
df.loc[df.sample(frac=0.2).index, 'Age'] = np.nan #20%
df.loc[df.sample(frac=0.002).index, 'Embarked'] = np.nan #0.2%

print('\n加入缺失值後的資料:')
print(df.head())

# 查看shape
print('\n資料形狀:', df.shape)

# data explore analysis
print('\n資料探索:')
print(df.head())
print(df.tail(10))

# 統計上的數據
print('\n數值統計資訊:')
print(df.describe())

print('\n非數值統計資訊:')
print(df.describe(include="object"))

# 取得所有欄位名稱
print('\n欄位名稱:', df.columns.tolist())

# 計數欄位資料值
print('\nSurvived 分布:')
print(df['Survived'].value_counts())

print('\nPclass 分布:')
print(df['Pclass'].value_counts().sort_index())

# matplot繁體中文字的設定
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.sans-serif"] = ["DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False
import seaborn as sns

# 提供字型列表
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Microsoft YaHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

missing_summary = pd.DataFrame({
    '遺失數量': df.isnull().sum(),
    '遺失比例': (df.isnull().sum() / len(df) *100).round(2)
})
print('\n缺失值統計:')
print(missing_summary)

missing_summary = missing_summary[missing_summary['遺失數量'] > 0]
print('\n有缺失值的欄位:')
print(missing_summary)

# 視覺化處理
plt.figure(figsize=(10, 6))
missing_summary['遺失比例'].plot(kind='barh', color='coral')
plt.xlabel('遺失比例 %')
plt.title('個欄位的遺失比例')
# plt.tight_layout()
# # plt.savefig('missing_values.png')  # 保存圖表
print('\n已保存缺失值圖表: missing_values.png')
plt.show()

# 刪除欄位
df_clean = df.drop('Cabin', axis=1)
print('\n刪除 Cabin 欄位後，剩餘欄位數:', df_clean.shape[1])

# Age: 採用中位數填補
age_median = df_clean['Age'].median()
df_clean['Age'] = df_clean['Age'].fillna(age_median)

# Embarked: 採用眾數填補
embarked_mode = df_clean['Embarked'].mode()[0]
df_clean['Embarked'] = df_clean['Embarked'].fillna(embarked_mode)

# 檢查清理後的資料
print('\n清理後的缺失值統計:')
print(df_clean.isnull().sum())

# 處理重複值
print('\n重複值數量:', df_clean.duplicated().sum())
df_clean.drop_duplicates(inplace=True)
print('刪除重複值後資料形狀:', df_clean.shape)

# 異常值檢測
print('\nFare 票價統計:')
print(df_clean['Fare'].describe())

# IQR : 異常值判斷
Q1 = df_clean['Fare'].quantile(0.25)
Q3 = df_clean['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df_clean[(df_clean['Fare'] < lower_bound) | (df_clean['Fare'] > upper_bound)]
print(f"\n票價異常值數量: {len(outliers)}")

# 特徵工程
print("=" * 60)
print("=" * 60)
# 1. 創建家庭人數特徵
df_clean['FamilySize'] = df_clean['SibSp'] + df_clean['Parch'] + 1
print("1. 創建 FamilySize (家庭人數) 特徵")
print(df_clean[['SibSp', 'Parch', 'FamilySize']].head())

# 2. 創建是否獨自一人特徵
df_clean['IsAlone'] = (df_clean['FamilySize'] == 1).astype(int)
print("\n2. 創建 IsAlone (是否獨自) 特徵")
print(df_clean[['FamilySize', 'IsAlone']].head())

# 年齡分組
def age_group(age):
    if pd.isna(age):
        return '未知'
    elif age < 12:
        return '兒童'
    elif age < 18:
        return '青少年'
    elif age < 60:
        return '成年人'
    else:
        return '老人'

df_clean['AgeGroup'] = df_clean['Age'].apply(age_group)
print("\n年齡分組分布:")
print(df_clean['AgeGroup'].value_counts())

# 特徵編碼
sex_mapping = {'male': 0, 'female':1}
df_clean['Sex_Encoded'] = df_clean['Sex'].map(sex_mapping)
print("\n性別編碼範例:")
print(df_clean[['Sex', 'Sex_Encoded']].head())

# one-hot encoding
embarked_dummies = pd.get_dummies(df_clean['Embarked'], prefix='Embarked')
df_clean = pd.concat([df_clean, embarked_dummies], axis=1)
print("\nEmbarked One-Hot 編碼範例:")
print(df_clean[['Embarked', 'Embarked_C', 'Embarked_Q', 'Embarked_S']].head())

# 保存清洗後的數據
df_clean.to_csv('cleaned_titanic.csv', index=False)
print("\n已保存清洗後的數據: cleaned_titanic.csv")

# 創建數據目錄並移動文件
import os
import shutil

# 確保目錄存在
os.makedirs('data', exist_ok=True)

# 移動文件，如果存在的話
if os.path.exists('titanic.csv'):
    shutil.move('titanic.csv', 'data/titanic.csv')
    print(f"已移動 titanic.csv 到 data/ 目錄")
else:
    print("titanic.csv 不存在")

if os.path.exists('cleaned_titanic.csv'):
    shutil.move('cleaned_titanic.csv', 'data/cleaned_titanic.csv')
    print(f"已移動 cleaned_titanic.csv 到 data/ 目錄")
else:
    print("cleaned_titanic.csv 不存在")
# ========== 缺失值處理前後對比 ==========
print("\n" + "=" * 60)
print("缺失值處理前後對比")
print("=" * 60)

# 處理前的缺失值
print("\n處理前的缺失值統計:")
missing_before = df.isnull().sum()
missing_before_percent = (missing_before / len(df)) * 100
missing_before_df = pd.DataFrame({
    '缺失數量': missing_before,
    '缺失比例%': missing_before_percent.round(2)
})
print(missing_before_df[missing_before_df['缺失數量'] > 0])

# 處理後的缺失值
print("\n處理後的缺失值統計:")
missing_after = df_clean.isnull().sum()
missing_after_percent = (missing_after / len(df_clean)) * 100
missing_after_df = pd.DataFrame({
    '缺失數量': missing_after,
    '缺失比例%': missing_after_percent.round(2)
})
print(missing_after_df[missing_after_df['缺失數量'] > 0])

# 可視化對比
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
missing_before_df['缺失比例%'].plot(kind='bar', color='lightcoral')
plt.title('處理前缺失值比例')
plt.ylabel('缺失比例 %')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
missing_after_df['缺失比例%'].plot(kind='bar', color='lightgreen')
plt.title('處理後缺失值比例')
plt.ylabel('缺失比例 %')
plt.xticks(rotation=45)

# plt.tight_layout()
# # plt.savefig('missing_values_comparison.png')
plt.show()
print("✅ 缺失值對比圖已保存: missing_values_comparison.png")

# ========== 保存處理過程的中間文件 ==========
print("\n" + "=" * 60)
print("保存處理結果")
print("=" * 60)

# 保存原始數據（如果不存在）
if not os.path.exists('data/raw_titanic.csv'):
    df.to_csv('data/raw_titanic.csv', index=False)
    print("✅ 原始數據已保存: data/raw_titanic.csv")

# 保存清洗後數據
df_clean.to_csv('data/cleaned_titanic.csv', index=False)
print("✅ 清洗後數據已保存: data/cleaned_titanic.csv")

# 保存特徵工程後的數據
df_fe = df_clean.copy()  # 創建特徵工程版本
print("✅ 特徵工程數據準備完成")

print("\n📊 數據處理總結:")
print(f"原始數據: {df.shape}")
print(f"清洗後數據: {df_clean.shape}")
print(f"新增特徵: {list(set(df_clean.columns) - set(df.columns))}")

print("\n🎉 數據清洗和特徵工程完成！")
print("下一步: 運行 pca.py 進行 PCA 分析")


# 主程序保護
if __name__ == "__main__":
    main()


# 主程序保護
if __name__ == "__main__":
    main()
