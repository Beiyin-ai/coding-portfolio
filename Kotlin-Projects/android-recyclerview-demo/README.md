# Android RecyclerView Demo

一個展示 Android RecyclerView 基本用法的 Kotlin 範例專案。

## 功能特色
- 📱 使用 RecyclerView 顯示列表項目
- 👆 點擊項目跳轉到詳細頁面
- 🔧 使用 ViewBinding 簡化視圖操作
- 📊 支援 GridLayoutManager (2列)
- 🔄 生成100筆假資料展示

## 技術棧
- **語言**: Kotlin
- **UI**: RecyclerView, ViewBinding
- **架構**: 簡單的 Activity + Adapter 模式

## 專案結構
```
app/src/main/kotlin/com/example/myapplication_0920/
├── MainActivity.kt          # 主畫面，包含 RecyclerView
├── DetailActivity.kt        # 詳細資訊畫面
├── SampleItem.kt            # 資料模型
└── SampleItemAdapter.kt     # RecyclerView 適配器

app/src/main/res/layout/
├── activity_main.xml        # 主畫面佈局
├── activity_detail.xml      # 詳細畫面佈局
└── item_list.xml            # 列表項目佈局
```

## 如何執行
1. Clone 專案
2. 用 Android Studio 開啟
3. 等待 Gradle 同步完成
4. 執行程式

## 授權
MIT License
