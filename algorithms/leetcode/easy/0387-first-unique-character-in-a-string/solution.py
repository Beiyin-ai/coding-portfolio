from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        找出第一個不重複字符的索引
        
        新解法：使用 Counter 統計頻率，然後遍歷計數字典
        更清晰易懂，充分利用 Python 標準庫
        """
        count = Counter(s)
        
        # 遍歷計數字典，找到第一個頻率為 1 的字符
        for key, value in count.items():
            if value == 1:
                return s.index(key)
        
        return -1
