from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Fizz Buzz 問題的更簡潔解法

        使用列表推導式、字串乘法和邏輯運算
        非常 Pythonic 的寫法
        """
        return [
            ("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i)
            for i in range(1, n + 1)
        ]
