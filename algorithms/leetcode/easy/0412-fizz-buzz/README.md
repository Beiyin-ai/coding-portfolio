# 412. Fizz Buzz

## 問題描述
給定整數 n，返回字串陣列 answer (1-indexed)，其中：
- 如果 i 能被 3 和 5 整除 → "FizzBuzz"
- 如果 i 能被 3 整除 → "Fizz"
- 如果 i 能被 5 整除 → "Buzz"
- 否則 → i（轉為字串）

## 解法

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
1. 建立一個空列表儲存結果
2. 遍歷 1 到 n 的所有數字
3. 檢查每個數字的整除條件
4. 根據條件添加對應的字串到結果中

### 複雜度分析
- **時間複雜度：O(n)**，需要遍歷 n 個數字
- **空間複雜度：O(n)**，需要儲存 n 個字串

## 測試結果
```
n = 3: ['1', '2', 'Fizz']
n = 5: ['1', '2', 'Fizz', '4', 'Buzz']
n = 15: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```
