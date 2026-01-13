from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ 尋找最長共同前綴
        
        使用第一個字串作為初始前綴，逐步與其他字串比較並縮短
        這是我的解法，直觀且效率良好
        """
        if not strs:
            return ""
        
        # 使用第一個字串作為初始前綴
        prefix = strs[0]
        
        for s in strs[1:]:
            # 逐步縮短前綴直到符合當前字串
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix
