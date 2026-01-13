"""
Titanic 數據分析主程序
包含數據生成、清洗和特徵工程功能
"""

# 產生titanic資料集
import numpy as np
import pandas as pd

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

print(df)

# Age, Embarked, Cabin: 有缺失值
# 隨機寫入缺失值
df.loc[df.sample(frac=0.2).index, 'Age'] = np.nan #20%
df.loc[df.sample(frac=0.002).index, 'Embarked'] = np.nan #0.2%

print(df)

# 查看shape
print(df.shape)

# data explore analysis
print(df.head()) #顯示前5筆資料
print(df.tail(10)) #顯示後5筆資料

# 統計上的數據
print(df.describe()) # 處理數值欄位的統計資訊

print(df.describe(include="object")) # 處理非數值欄位的統計資訊

# 取得所有欄位名稱
print(df.columns)

# 計數欄位資料值
# 單一欄位的篩選 df['column name']
print(df['Survived'].value_counts())
print(df['Pclass'].value_counts().sort_index())

# 多欄位的篩選 df[['col1, col5, col10,...']]
print(df[['Name', 'Sex', 'Ticket']])

# 根據欄位值進行篩選 df[df['col name'] > 50]
print(df[df['Age'] > 60].head())

# 篩選多個條件
print(df[ (df['Sex'] == 'female') & (df['Pclass'] == 1)].head(10))
print(f"{df[ (df['Sex'] == 'female') & (df['Pclass'] == 1)]['Survived'].mean():.2%}") # 53.25%

# isin(): 欄位值的挑選
print(df[ df['Embarked'].isin(['C', 'Q'])])


# matplot繁體中文字的設定
import matplotlib.pyplot as plt
import seaborn as sns

# 提供字型列表
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Microsoft YaHei']

# 定義字型使用無櫬字型
plt.rcParams['font.family'] = 'sans-serif'

# 處理中文 '-'顯示問題
plt.rcParams['axes.unicode_minus'] = False

missing_summary = pd.DataFrame({
    '遺失數量': df.isnull().sum(),
    '遺失比例': (df.isnull().sum() / len(df) *100).round(2)
})
print(missing_summary)

missing_summary = missing_summary[missing_summary['遺失數量'] > 0]

print(missing_summary)

# 視覺化處理
# 先產生畫布
plt.figure(figsize=(10, 6))
missing_summary['遺失比例'].plot(kind='barh', color='coral')
plt.xlabel('遺失比例 %')
plt.title('個欄位的遺失比例')
plt.tight_layout()
plt.show()

# 刪除欄位
df_clean = df.drop('Cabin', axis=1)
print(df_clean.shape[1])

# Age: 採用中位數填補
age_median = df_clean['Age'].median()
# inplace寫回原始的df
df_clean['Age'].fillna(age_median, inplace=True)

# Embarked: 採用眾數填補
embarked_mode = df_clean['Embarked'].mode()[0]
df_clean['Embarked'].fillna(embarked_mode, inplace=True)

# 檢查清理後的資料
print(df_clean.isnull().sum())


# 處理重複值
print(df_clean.duplicated().sum())
df_clean.drop_duplicates(inplace=True)


print(df_clean['Fare'].describe())
plt.figure(figsize=(12,5))
# 第一張子圖
plt.subplot(1, 2 ,1)
# 箱型圖
plt.boxplot(df_clean['Fare'])
plt.title('票價盒鬚圖')
plt.ylabel('票價')

# 第二張子圖
plt.subplot(1, 2 ,2)
# 直方圖
plt.hist(df_clean['Fare'], bins=50, color='skyblue', edgecolor='black')
plt.title('票價分布直方圖')
plt.xlabel('票價')
plt.ylabel('人數')
plt.tight_layout()
plt.show()


# IQR : 異常值判斷
Q1 = df_clean['Fare'].quantile(0.25)
Q3 = df_clean['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df_clean[(df_clean['Fare'] < lower_bound) | (df_clean['Fare'] > upper_bound)]
print(f"異常值: {len(outliers)}")

# 特徵創建 - 家庭人數
print("=" * 60)
print(" 特徵工程示範")
print("=" * 60)
# 1. 創建家庭人數特徵
df_clean['FamilySize'] = df_clean['SibSp'] + df_clean['Parch'] + 1
print("1. 創建 FamilySize (家庭人數) 特徵")
print(df_clean[['SibSp', 'Parch', 'FamilySize']].head())
# 2. 創建是否獨自一人特徵
df_clean['IsAlone'] = (df_clean['FamilySize'] == 1).astype(int)
print("\n2. 創建 IsAlone (是否獨自) 特徵")
print(df_clean[['FamilySize', 'IsAlone']].head())

# 將原始資料進行分組
# 定義分組原則
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
print(df_clean['AgeGroup'].value_counts())


# 特徵編碼: 非數值的資料傳換成數值資料
# 標籤編碼: 0,1,2,...
# 轉換表
sex_mapping = {'male': 0, 'female':1}
df_clean['Sex_Encoded'] = df_clean['Sex'].map(sex_mapping)
print(df_clean[['Sex', 'Sex_Encoded']].head())

# one-hot code
# get_dummies
embarked_dummies = pd.get_dummies(df_clean['Embarked'], prefix='Embarked')
# 不同資料表的合併
df_clean = pd.concat([df_clean, embarked_dummies], axis=1)
print(df_clean[['Embarked', 'Embarked_C', 'Embarked_Q', 'Embarked_S']].head())


# 建立不同表格
sales = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104],
    'SalesAmount':[1000, 1500, 200, 500]
})

customers = pd.DataFrame({
    'CustomerID': [101, 103, 105],
    'Region':['N', 'S', 'E']
})

print(f"sales:{sales}")
print(f"customers:{customers}")

# Inner Join
merged_inner = pd.merge(sales, customers, on='CustomerID', how='inner')
print(f"merged_inner: {merged_inner}")

# left Join: 以左邊的資料表為主(sales)
merged_left = pd.merge(sales, customers, on='CustomerID', how='left')
print(f"merged_left: {merged_left}")



# groupby
# 單一分組, 單一聚合
age_avg_by_class = df_clean.groupby('Pclass')['Age'].mean()
print(f"age_avg_by_class: {age_avg_by_class}")

# 單一分組, 多種聚合
multi_by_class = df_clean.groupby('Pclass')['Fare'].agg(['count', 'mean', 'std', 'min', 'max'])
print(f"multi_by_class: {multi_by_class}")

# 多種分組
multi_group_by_class = df_clean.groupby(['Pclass','Sex'])['Survived'].mean()
print(f"age_avg_by_class: {multi_group_by_class}")

# 樞紐分析表
pivot_table = df_clean.pivot_table(values='Survived', index='Pclass', columns='Sex', aggfunc='mean')
print(f"pivot_table: {pivot_table}")


# hrat map: 相關性分析
numerical_columns = ['Survived', 'Pclass', 'Age','SibSp', 'Parch', 'Fare', 'FamilySize', 'IsAlone']
correlation = df_clean[numerical_columns].corr()

plt.figure(figsize=(10,8))

sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Heat Map', fontsize=16)
plt.tight_layout()
plt.show()
