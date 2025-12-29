"""
412. Fizz Buzz

解法：基本條件判斷法
時間複雜度：O(n)
空間複雜度：O(n)
"""

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        基本解法：使用條件判斷
        """
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

# 測試程式碼
if __name__ == "__main__":
    solution = Solution()

    test_cases = [3, 5, 15]
    for n in test_cases:
        print(f"n = {n}: {solution.fizzBuzz(n)}")
