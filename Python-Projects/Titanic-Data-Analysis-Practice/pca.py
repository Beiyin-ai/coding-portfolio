import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.sans-serif"] = ["DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Microsoft YaHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

print("開始 PCA 分析...")

# 讀取清洗後的數據
try:
    df = pd.read_csv('data/cleaned_titanic.csv')
    print("成功讀取 cleaned_titanic.csv")
except FileNotFoundError:
    print("未找到清洗後的數據，請先運行 app.py")
    exit()

# 複製數據進行特徵工程
df_fe = df.copy()

# 目標變數
TARGET = "Survived"

# 創建新特徵
df_fe['family_size'] = df_fe['SibSp'] + df_fe['Parch']
df_fe["is_female"] = (df_fe["Sex"] == "female").astype(int)

print("\n特徵工程後數據形狀:", df_fe.shape)
print("特徵工程後數據預覽:")
print(df_fe.head())

# 選擇用於 PCA 的特徵
numeric_features = ['Age', 'Fare', 'family_size', 'is_female', 'Pclass']
categorical_features = ['Embarked']

print("\n數值特徵:", numeric_features)
print("類別特徵:", categorical_features)

# 定義 pipeline 對於數值資料的預處理
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

# 定義 pipeline 對於類別資料的預處理
categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ]
)

# 合併預處理步驟
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# PCA 設定
pca = PCA(n_components=0.95, random_state=42)

# 完整的流水線
pipeline = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("pca", pca)
    ]
)

# PCA 開始從資料中學習重要特徵
print("\n執行 PCA 分析...")
X_pca = pipeline.fit_transform(df_fe)

# 輸出 PCA 結果
print(f"原始特徵數量: {len(numeric_features) + len(categorical_features)}")
print(f"PCA 後保留的特徵數量: {X_pca.shape[1]}")

# 獲取 PCA 模型
pca_model = pipeline.named_steps["pca"]
print("\n各主成分解釋的變異比例:")
for i, ratio in enumerate(pca_model.explained_variance_ratio_, 1):
    print(f"  主成分 {i}: {ratio:.3f}")

total_variance = pca_model.explained_variance_ratio_.sum()
print(f"累積解釋變異比例: {total_variance:.3f}")

# 可視化 PCA 結果
plt.figure(figsize=(10, 8))

# 主成分可視化
plt.subplot(2, 1, 1)
plt.bar(range(1, len(pca_model.explained_variance_ratio_) + 1),
        pca_model.explained_variance_ratio_)
plt.xlabel('主成分')
plt.ylabel('解釋變異比例')
plt.title('各主成分解釋的變異比例')
plt.grid(True, alpha=0.3)

# PCA 散點圖
plt.subplot(2, 1, 2)
scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=df_fe[TARGET],
    alpha=0.7,
    cmap='coolwarm'
)
plt.xlabel('第一主成分 (PCA1)')
plt.ylabel('第二主成分 (PCA2)')
plt.title('PCA 散點圖 (根據是否存活著色)')
plt.colorbar(scatter, label='Survived (0=死亡, 1=存活)')
plt.grid(True, alpha=0.3)

# plt.tight_layout()
# # plt.savefig('pca_analysis.png')
print("\nPCA 圖表已保存為 pca_analysis.png")
plt.show()

# 保存 PCA 結果
pca_df = pd.DataFrame(X_pca, columns=[f'PC{i+1}' for i in range(X_pca.shape[1])])
pca_df['Survived'] = df_fe[TARGET].values
pca_df.to_csv('pca_results.csv', index=False)
print("PCA 結果已保存為 pca_results.csv")

print("\nPCA 分析完成！")


# 主程序保護
if __name__ == "__main__":
    main()


# 主程序保護
if __name__ == "__main__":
    main()
