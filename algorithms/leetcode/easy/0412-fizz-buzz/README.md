# 412. Fizz Buzz

**完成日期：** 2025-12-27（首次完成），2026-01-02（優化更新）  

**難度：** Easy  
**標籤：** Math, String, Simulation  
**連結：** [LeetCode 412](https://leetcode.com/problems/fizz-buzz/)

## 題目描述
Given an integer `n`, return a string array `answer` (1-indexed) where:

- `answer[i] == "FizzBuzz"` if `i` is divisible by `3` and `5`.
- `answer[i] == "Fizz"` if `i` is divisible by `3`.
- `answer[i] == "Buzz"` if `i` is divisible by `5`.
- `answer[i] == i` (as a string) if none of the above conditions are true.

### 範例
**範例 1：**
```
Input: n = 3
Output: ["1","2","Fizz"]
```

**範例 2：**
```
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
```

**範例 3：**
```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

### 限制條件
- `1 <= n <= 10^4`

## 解法 1：我的新解法（更簡潔 Pythonic）

### 程式碼
```python
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            ("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i)
            for i in range(1, n + 1)
        ]
```

### 解題思路
1. **使用列表推導式**：`[expression for i in range(1, n+1)]`
2. **巧妙利用布林值乘法**：`"Fizz" * (i % 3 == 0)` 當條件為真時得到 "Fizz"，為假時得到空字串
3. **使用邏輯運算**：`or str(i)` 當前面為空字串時，返回數字的字串表示

### 關鍵技巧
- **布林值可當 0/1 使用**：Python 中 `True == 1`，`False == 0`
- **字串乘法**：`"Fizz" * 1 = "Fizz"`，`"Fizz" * 0 = ""`
- **短路求值**：`or` 運算子的特性

## 解法 2：我原本的解法（基礎易懂）

### 程式碼
```python
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
```

### 解題思路
1. **創建空列表**：儲存結果
2. **遍歷 1 到 n**：使用 for 迴圈
3. **條件判斷**：按照題目要求檢查每個數字
4. **添加結果**：根據條件添加對應的字串

### 解題思路比較
| 方法 | 程式碼長度 | 可讀性 | Python 技巧 | 學習價值 |
|------|-----------|--------|-------------|----------|
| 新解法（列表推導式） | 最短 | 中等（需要理解技巧） | 高級 | 學習 Python 進階語法 |
| 原本解法（for 迴圈） | 較長 | 高（直觀易懂） | 基礎 | 學習基礎邏輯控制 |

### 複雜度分析
- **時間複雜度：O(n)** - 需要遍歷 1 到 n
- **空間複雜度：O(n)** - 需要儲存 n 個結果

### 測試範例
```python
測試 1: n = 3 → ["1", "2", "Fizz"]
測試 2: n = 5 → ["1", "2", "Fizz", "4", "Buzz"]
測試 3: n = 15 → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
```
