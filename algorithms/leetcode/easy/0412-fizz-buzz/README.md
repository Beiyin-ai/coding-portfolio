# 412. Fizz Buzz

## 問題描述
給定整數 n，返回字串陣列 answer (1-indexed)，其中：
- 如果 i 能被 3 和 5 整除 → "FizzBuzz"
- 如果 i 能被 3 整除 → "Fizz"
- 如果 i 能被 5 整除 → "Buzz"
- 否則 → i（轉為字串）

## 解法
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