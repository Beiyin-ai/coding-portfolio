class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        最長不重複子字串
        
        解法：滑動窗口 (Sliding Window) + 集合 (Set)
        時間複雜度：O(n)
        空間複雜度：O(min(n, m))，m 是字符集大小
        """
        seen = set()    # 記錄當前窗口中的字符
        left = 0        # 窗口左指針
        max_len = 0     # 最長長度
        
        for right in range(len(s)):
            # 如果當前字符已存在，移動左指針直到字符不再重複
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # 加入當前字符到集合
            seen.add(s[right])
            
            # 更新最大長度
            max_len = max(max_len, right - left + 1)
        
        return max_len
