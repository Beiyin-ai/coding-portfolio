# 1672. Richest Customer Wealth

## 問題描述
給定一個 m x n 的整數網格 accounts，其中 accounts[i][j] 是第 i 位客戶在第 j 家銀行的存款金額。
返回最富有客戶的財富總量。

## 解法

### 程式碼
```python
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for items in accounts:
            current = 0
            for nums in items:
                current += nums
                if current > richest:
                    richest = current
        return richest
```

### 解題思路
1. 初始化 richest = 0 記錄最大財富
2. 遍歷每個客戶（外層迴圈）
3. 對每個客戶計算財富總和（內層迴圈）
4. 在計算過程中即時更新最大值
5. 返回最大值

### 複雜度分析
- **時間複雜度：O(n×m)**，n 為客戶數，m 為銀行數
- **空間複雜度：O(1)**，只使用常數空間

## 測試結果
所有測試案例都通過！✓
