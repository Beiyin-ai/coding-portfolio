# 專案設定指南

## 檔案結構說明
rock-paper-scissors/
├── README.md                    # 專案說明文件
├── build.gradle.kts             # Gradle 建置設定
└── app/
    ├── src/main/kotlin/com/example/pss_1027/
    │   └── MainActivity.kt      # 主程式邏輯
    └── src/main/res/layout/
        └── activity_main.xml    # 使用者介面佈局

## 主要修改
1. 比分顯示優化：將原本兩行的比分顯示改為單行顯示
2. 程式碼結構化：將遊戲邏輯分為玩家回合和電腦回合
3. 狀態管理：使用布林值追蹤輪替順序

## 執行測試
如需在 Android Studio 中測試：
1. 開啟 Android Studio
2. 選擇 "Open an existing project"
3. 導航至 rock-paper-scissors 資料夾
4. 等待 Gradle 同步完成
5. 點擊 Run 按鈕執行

## 已知問題
- 目前比分顯示在某些情況下可能超出螢幕範圍
- 電腦的隨機演算法較為簡單，可考慮加入 AI 邏輯

## 未來改進建議
1. 加入動畫效果
2. 增加音效
3. 支援多語言
4. 加入遊戲紀錄功能
5. 可調整難度等級
