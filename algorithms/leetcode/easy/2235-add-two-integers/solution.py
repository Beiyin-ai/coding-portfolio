# 2235. Add Two Integers

class Solution:
    def sum_operator(self, num1: int, num2: int) -> int:
        """直接使用加法運算子"""
        return num1 + num2

    def sum_bitwise(self, num1: int, num2: int) -> int:
        """位元運算解法（學習用）"""
        # 當進位不為0時繼續
        while num2 != 0:
            # 計算進位
            carry = num1 & num2
            # 計算不帶進位的和
            num1 = num1 ^ num2
            # 進位左移一位
            num2 = carry << 1
        return num1

    # LeetCode 要求的方法
    def sum(self, num1: int, num2: int) -> int:
        return self.sum_operator(num1, num2)

# 測試程式碼
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (12, 5),
        (-10, 4),
        (0, 0),
        (100, -100)
    ]

    print("=== Add Two Integers 測試 ===")
    for num1, num2 in test_cases:
        result1 = solution.sum_operator(num1, num2)
        result2 = solution.sum_bitwise(num1, num2)

        print(f"輸入: {num1} + {num2}")
        print(f"加法運算: {result1}")
        print(f"位元運算: {result2}")
        print(f"結果相同: {result1 == result2}")
        print()
