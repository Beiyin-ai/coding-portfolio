682. Baseball Game
完成日期： 2026-01-27
難度： Easy
標籤： Array, Stack, Simulation
連結： LeetCode 682

## 題目描述
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

1. **An integer x** - Record a new score of x.
2. **'+'** - Record a new score that is the sum of the previous two scores.
3. **'D'** - Record a new score that is the double of the previous score.
4. **'C'** - Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

## 範例
**範例 1：**
```
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
```

**範例 2：**
```
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
```

**範例 3：**
```
Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
```

## 限制條件
- 1 <= operations.length <= 1000
- operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
- For operation "+", there will always be at least two previous scores on the record.
- For operations "C" and "D", there will always be at least one previous score on the record.
- The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer.

## 解法：模擬操作（我的解法）
### 程式碼
```python
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """ 棒球遊戲計分

        使用數組模擬遊戲記錄的變化
        根據不同的操作進行相應的處理
        這是我的解法
        """
        record = []

        for op in operations:
            if op == "C":
                # 移除最後一個分數
                record.pop()
            elif op == "D":
                # 將最後一個分數乘以2後加入
                record.append(record[-1] * 2)
            elif op == "+":
                # 將最後兩個分數相加後加入
                record.append(record[-1] + record[-2])
            else:
                # 將字串轉為整數後加入
                record.append(int(op))
        
        return sum(record)
```

### 解題思路
1. **初始化記錄**：建立一個空數組來儲存分數
2. **遍歷操作**：對每個操作進行相應處理：
   - `"C"`：移除最後一個分數（使用 `pop()`）
   - `"D"`：將最後一個分數乘以2後加入
   - `"+"`：將最後兩個分數相加後加入
   - 數字：轉為整數後加入
3. **計算總和**：最後返回所有分數的總和

### 複雜度分析
- **時間複雜度**：O(n)
  - 需要遍歷一次 operations 數組
  - 每個操作都是 O(1) 時間
  - n 是 operations 的長度
- **空間複雜度**：O(n)
  - 最壞情況下需要儲存所有分數
  - record 數組的大小最多為 n

## 我的思考過程
### 第一階段：理解規則
1. **閱讀題目**：仔細理解每種操作的意義
2. **分析範例**：透過範例了解操作的執行順序和效果
3. **確認邊界**：注意題目保證操作都是有效的

### 第二階段：設計解法
1. **選擇數據結構**：使用數組（列表）來儲分數記錄
2. **處理每種操作**：
   - 數字：直接轉換並加入
   - `"C"`：移除最後一個元素
   - `"D"`：存取最後一個元素並計算
   - `"+"`：存取最後兩個元素並計算
3. **考慮效率**：使用 Python 列表的 `append()` 和 `pop()` 都是 O(1) 操作

### 第三階段：實現和測試
1. **實現程式碼**：按照設計寫出解法
2. **測試範例**：確保通過所有提供的範例
3. **考慮邊界**：雖然題目保證操作有效，但可以思考如果操作無效時該如何處理

## 關鍵點
### 1. 數據結構選擇
- **數組/列表**：支援快速存取最後一個和最後第二個元素
- **棧（Stack）**：這實際上是棧的應用，但 Python 列表可以很好地模擬棧

### 2. 操作處理
- **`"C"`**：使用 `pop()` 移除最後一個元素
- **`"D"`**：使用 `record[-1]` 存取最後一個元素
- **`"+"`**：使用 `record[-1] + record[-2]` 計算和
- **數字**：使用 `int(op)` 轉換字串

### 3. 邊界條件
- **空記錄**：範例3顯示記錄可以為空
- **負數**：分數可以是負數
- **大數字**：所有計算都在 32-bit 整數範圍內

## 測試範例
### 測試 1：基本操作
- Input: ["5","2","C","D","+"]
- 過程：
  1. 5 → [5]
  2. 2 → [5, 2]
  3. C → [5]
  4. D → [5, 10]
  5. + → [5, 10, 15]
  6. 總和：5 + 10 + 15 = 30

### 測試 2：包含負數和多次操作
- Input: ["5","-2","4","C","D","9","+","+"]
- 總和：5 + (-2) + (-4) + 9 + 5 + 14 = 27

### 測試 3：簡單操作
- Input: ["1","C"]
- 過程：
  1. 1 → [1]
  2. C → []
  3. 總和：0

### 測試 4：連續加分
- Input: ["5","2","+","D","C"]
- 過程：
  1. 5 → [5]
  2. 2 → [5, 2]
  3. + → [5, 2, 7]
  4. D → [5, 2, 7, 14]
  5. C → [5, 2, 7]
  6. 總和：5 + 2 + 7 = 14

## 學習心得
這題讓我學到：
1. **問題理解**：仔細閱讀題目，理解每種操作的具體含義
2. **模擬思維**：將現實世界的規則轉化為程式邏輯
3. **數據結構選擇**：根據操作特性選擇合適的數據結構（棧/數組）
4. **邊界條件**：雖然題目保證操作有效，但仍需思考潛在的邊界情況
5. **代碼清晰度**：使用清晰的條件判斷和有意義的變數名稱

## 相關題目
- **150. Evaluate Reverse Polish Notation** (Medium) - 類似的中綴表達式求值
- **739. Daily Temperatures** (Medium) - 棧的應用
- **155. Min Stack** (Medium) - 設計具有特殊功能的棧
- **844. Backspace String Compare** (Easy) - 類似「C」操作的字串處理

## 下一步計畫
1. 嘗試 **150. Evaluate Reverse Polish Notation**（波蘭表達式求值）
2. 練習更多棧相關的題目
3. 學習更複雜的模擬類題目
