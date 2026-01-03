# 1672. Richest Customer Wealth

**完成日期：** 2025-12-25（首次完成），後續優化  

**難度：** Easy  
**標籤：** Array, Matrix  
**連結：** [LeetCode 1672](https://leetcode.com/problems/richest-customer-wealth/)

## 題目描述
You are given an `m x n` integer grid `accounts` where `accounts[i][j]` is the amount of money the `i-th` customer has in the `j-th` bank. Return the **wealth** that the richest customer has.

A customer's **wealth** is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum **wealth**.

### 範例
**範例 1：**
```
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each.
```

**範例 2：**
```
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
```

**範例 3：**
```
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
```

### 限制條件
- `m == accounts.length`
- `n == accounts[i].length`
- `1 <= m, n <= 50`
- `1 <= accounts[i][j] <= 100`

## 解法 1：我的新解法（更簡潔）

### 程式碼
```python
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)
```

### 解題思路
1. **計算每位客戶的總財富**：使用 `sum()` 計算每個客戶的所有銀行存款
2. **找出最大值**：使用 `max()` 函數找出最大的總財富
3. **使用生成器表達式**：`(sum(customer) for customer in accounts)` 產生每位客戶的財富值

### 學習進步
我原本的解法使用了 for 迴圈和變數，現在學到了更簡潔的寫法：
- **生成器表達式**：更節省記憶體
- **一行解決**：程式碼更簡潔易讀
- **Python 內建函數**：充分利用 `sum()` 和 `max()`

## 解法 2：我原本的解法

### 程式碼
```python
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
```

### 解題思路
1. **初始化最大財富**：設定 `max_wealth = 0`
2. **遍歷每位客戶**：計算每位客戶的總財富
3. **更新最大值**：如果當前客戶財富大於最大值，則更新
4. **返回結果**：返回最大財富值

### 解題思路比較
| 方法 | 程式碼長度 | 可讀性 | 學習價值 |
|------|-----------|--------|----------|
| 新解法（一行） | 最短 | 高（對熟悉 Python 的人） | 學習進階語法 |
| 原本解法 | 較長 | 高（對初學者） | 學習基礎邏輯 |

### 複雜度分析
- **時間複雜度：O(m × n)**
  - 需要遍歷每個客戶的每個銀行帳戶
  - `m`：客戶數量，`n`：銀行數量
- **空間複雜度：O(1)**
  - 只使用了常數額外空間

### 測試範例
```python
測試 1: [[1,2,3],[3,2,1]] → 6
測試 2: [[1,5],[7,3],[3,5]] → 10
測試 3: [[2,8,7],[7,1,3],[1,9,5]] → 17
測試 4: [[1]] → 1
測試 5: [[100,200],[300,400]] → 700
```

### 學習心得
這題讓我學到：
1. **從基礎到進階**：從原本的 for 迴圈解法，進步到一行簡潔寫法
2. **Python 生成器表達式**：`(expression for item in iterable)` 的應用
3. **內建函數的威力**：`sum()` 和 `max()` 的組合使用
4. **程式碼簡潔化**：思考如何用更少的程式碼達到相同效果

### 相關題目
- [1572. Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/) (Easy)
- [566. Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/) (Easy)
- [867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) (Easy)

### 下一步計畫
1. 嘗試用其他語言實現
2. 練習更多矩陣相關的題目
3. 學習更多 Python 的進階語法技巧
