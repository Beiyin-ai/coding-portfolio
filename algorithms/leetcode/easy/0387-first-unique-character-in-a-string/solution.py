class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        解法：使用 HashMap 統計字符頻率
        
        時間複雜度：O(n) - 兩次遍歷
        空間複雜度：O(1) - 只有26個小寫字母
        """
        count = {}
        
        # 第一次遍歷：統計每個字符出現次數
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        # 第二次遍歷：找第一個唯一字符
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1
