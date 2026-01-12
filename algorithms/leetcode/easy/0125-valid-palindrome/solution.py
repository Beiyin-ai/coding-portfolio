class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ 判斷是否為回文
        
        使用 Python 內建函式過濾非字母數字字元並轉小寫
        然後比較字串與其反轉是否相同
        這是我的解法，簡潔直觀
        """
        # 過濾非字母數字字元並轉為小寫
        palin = ''.join(ch.lower() for ch in s if ch.isalnum())
        # 比較字串與反轉字串
        return palin == palin[::-1]
