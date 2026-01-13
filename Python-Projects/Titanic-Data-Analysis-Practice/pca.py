"""
PCA 主成分分析
用於 Titanic 數據的降維分析
"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer # 填補空缺值
from sklearn.preprocessing import OneHotEncoder, StandardScaler # 分類資料轉成數值, 標準差
from sklearn.compose import ColumnTransformer # 控制分流&整併
from sklearn.pipeline import Pipeline # 流水線
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# step1: 載入資料
df = pd.read_csv("Titanic-Dataset.csv")

#定義目標
TARGET = "Survived"

# 特徵工程
df_fe = df.copy()

# family size
df_fe['family_size'] = df_fe['SibSp'] + df_fe['Parch']

# 類別轉數值計算
df_fe["is_female"] = (df_fe["Sex"] == "female").astype(int)

numeric_feartures = ['Age', 'Fare', 'family_size', 'is_female', 'Pclass']
categorical_features = ["Embarked"]

# 定義pipeline 對於數值資料的預處理
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")), # 填空白值
        ("scaler", StandardScaler()) # 標準化
    ]
)

# 定義pipeline 對於類別資料的預處理
categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")), # 填空白值
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False)) # 標準化
    ]
)
# 流水線的分流與整併
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_feartures),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# PCA: (保留原始資料中絕大多數的資訊: 95%)
pca = PCA(n_components=0.95, random_state=42)

# 完整的流水線
pipeline = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("pca", pca)
    ]
)

# PCA 開始從資料中學習重要特徵
X_pca = pipeline.fit_transform(df_fe)

print(f"原始特徵: {len(numeric_feartures) + len(categorical_features)}")
print(f"pca後擷取的特徵: {X_pca.shape[1]}")


pca_model = pipeline.named_steps["pca"]
print(pca_model.explained_variance_ratio_)
print(pca_model.explained_variance_ratio_.sum())

plt.figure(figsize=(8,6))

scatter = plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c= df_fe[TARGET],
    alpha=0.7
)

plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.title("PCA with Survived")
plt.colorbar(scatter, label="Survived")
plt.grid()
plt.show()

all_feature_names = pipeline.named_steps["preprocess"].get_feature_names_out()
print(all_feature_names)

loading = pd.DataFrame(
    pca_model.components_.T,
    index=all_feature_names,
    columns=[f"PC{i+1}" for i in range(pca_model.n_components_)]
)

top_3_pca1 = loading['PC1'].abs().sort_values(ascending=False).head()

print(f"PC1的主要特徵: {top_3_pca1}")
