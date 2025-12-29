"""
LeetCode 9. Palindrome Number

解法 1：字串反轉法（簡單直觀）
時間複雜度：O(n)，n為數字位數
空間複雜度：O(n)，需要字串儲存
"""

class Solution:
    def isPalindrome_string(self, x: int) -> bool:
        """
        字串解法：將數字轉為字串，比較正反序
        
        優點：簡單易懂
        缺點：需要額外空間儲存字串
        """
        if x < 0:
            return False  # 負數不可能是回文數
        
        s = str(x)
        return s == s[::-1]
    
    def isPalindrome_math(self, x: int) -> bool:
        """
        數學解法：反轉數字後比較
        
        優點：空間複雜度 O(1)
        缺點：需要處理邊界條件
        """
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return original == reversed_num
    
    # LeetCode 要求的方法
    def isPalindrome(self, x: int) -> bool:
        return self.isPalindrome_string(x)


# 測試程式碼
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (12321, True),
        (12345, False),
    ]
    
    print("=== Palindrome Number 測試 ===")
    print(f"解法 1：字串反轉法 (O(n) 空間)")
    print(f"解法 2：數學反轉法 (O(1) 空間)\n")
    
    for i, (x, expected) in enumerate(test_cases, 1):
        result1 = solution.isPalindrome_string(x)
        result2 = solution.isPalindrome_math(x)
        
        status1 = "✓" if result1 == expected else "✗"
        status2 = "✓" if result2 == expected else "✗"
        
        print(f"測試 {i}: {status1}{status2}")
        print(f"  輸入: {x}")
        print(f"  預期: {expected}")
        print(f"  字串法: {result1}")
        print(f"  數學法: {result2}")
        print()
