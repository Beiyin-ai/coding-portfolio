# 9. Palindrome Number
# 解題日期: 13天前

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        return y == y[::-1]
