from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """ 反轉字串
        
        使用雙指針從兩端向中間交換元素
        這是我的解法，時間複雜度 O(n)，空間複雜度 O(1)
        """
        left = 0
        right = len(s) - 1
        
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
