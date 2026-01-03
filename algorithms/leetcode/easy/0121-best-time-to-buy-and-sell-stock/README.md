# 121. Best Time to Buy and Sell Stock

**完成日期：** 2026-01-03  

**難度：** Easy  
**標籤：** Array, Dynamic Programming  
**連結：** [LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## 題目描述
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### 範例
**範例 1：**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**範例 2：**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

### 限制條件
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## 解法 1：使用 min/max 函數（我的新寫法）

### 程式碼
```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
                
        return max_profit
```

### 解題思路
1. **維護兩個變數**：
   - `min_price`：到目前為止看到的最低價格
   - `max_profit`：到目前為止的最大利潤
   
2. **一次遍歷，使用內建函數**：
   - 使用 `min()` 函數更新最低價格
   - 使用 `max()` 函數更新最大利潤
   
3. **返回結果**：遍歷結束後返回 `max_profit`

### 優點
- **程式碼簡潔**：使用內建函數，減少條件判斷
- **可讀性高**：意圖明確，容易理解
- **效能相同**：時間複雜度仍是 O(n)

## 解法 2：使用 if-else 判斷（我的原始思路）

### 程式碼
```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
```

### 解題思路
1. **維護兩個變數**：同上
2. **一次遍歷，手動判斷**：
   - 如果當前價格更低，更新最低價格
   - 否則，計算當前利潤，如果更大則更新最大利潤
3. **返回結果**：同上

### 解題思路比較
| 方法 | 程式碼長度 | 可讀性 | Python 技巧 | 適用場景 |
|------|-----------|--------|-------------|----------|
| min/max 函數法 | 較短 | 高 | 使用內建函數 | 追求簡潔程式碼 |
| if-else 判斷法 | 較長 | 中等 | 基礎邏輯控制 | 理解演算法細節 |

### 複雜度分析
- **時間複雜度：O(n)**
  - 兩種解法都是 O(n)，只需一次遍歷
  - 每個元素處理一次
  
- **空間複雜度：O(1)**
  - 兩種解法都只使用兩個額外變數
  - 空間使用與輸入大小無關

### 測試範例
```python
測試 1: [7,1,5,3,6,4] → 5
測試 2: [7,6,4,3,1] → 0
測試 3: [1,2,3,4,5] → 4
測試 4: [3,2,1,2,3] → 2
測試 5: [2,4,1] → 2
```

### 學習心得
這題讓我學到：
1. **同一個問題的多種解法**：if-else vs min/max
2. **程式碼簡潔化**：使用內建函數讓程式碼更優雅
3. **貪心演算法的應用**：在遍歷中維護關鍵資訊
4. **效能考量**：兩種解法時間複雜度相同，但可讀性不同

### 相關題目
- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) (Medium)
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (Hard)
- [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) (Hard)

### 下一步計畫
1. 嘗試解決可以多次交易的股票問題
2. 練習更多貪心演算法的應用
3. 學習動態規劃解法
