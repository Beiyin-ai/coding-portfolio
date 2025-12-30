# Kotlin Sealed Class 學習筆記

## 學習目標
- 理解 Kotlin Sealed Class（密封類別）的用途
- 學習使用 Sealed Class 管理有限狀態
- 掌握 when 表達式與 Sealed Class 的配合

## 程式碼說明
這是一個訂單狀態管理的範例，展示如何使用 Sealed Class 來表示有限的訂單狀態。

### 狀態定義
- `Created`：訂單已建立
- `Paid`：已付款（包含付款方式）
- `Shipped`：已出貨（包含物流資訊）
- `Finished`：訂單完成
- `Cancelled`：訂單取消（包含取消原因）

### 技術重點
1. **Sealed Class**：確保所有狀態都在編譯時已知
2. **Data Class**：用於帶有額外資料的狀態
3. **Object**：用於單例狀態
4. **when 表達式**：型別安全的模式匹配

## 執行結果
```
=== Kotlin Sealed Class 範例 ===
Order created
Paid: Payment method: Credit Card
Shipped: Logistics company: Black Cat Express | Tracking code: T123456789
Order cancelled: Reason: User requested cancellation
Order completed
```

## 學習心得
Kotlin 的 Sealed Class 提供了一種型別安全的方式來管理有限狀態集合，
適合用於訂單流程、網路請求狀態、UI 狀態等場景。

## 擴展練習
1. 新增一個 `Refunded` 狀態
2. 為 `Shipped` 狀態添加預計送達時間
3. 實現狀態轉換函式（如 `payOrder()`, `shipOrder()`）

## 檔案資訊
- 檔案名稱：order-state.kt
- 行數：55 行
- 建立日期：2024-12-30
