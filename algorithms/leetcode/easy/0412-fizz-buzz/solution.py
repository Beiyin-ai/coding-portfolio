"""
412. Fizz Buzz

解題思路：
1. 遍歷 1 到 n 的所有數字
2. 檢查每個數字是否滿足條件
3. 根據條件返回對應的字串
"""

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


# 測試範例
if __name__ == "__main__":
    solution = Solution()
    
    # 測試案例
    test_cases = [3, 5, 15]
    for n in test_cases:
        print(f"n = {n}: {solution.fizzBuzz(n)}")