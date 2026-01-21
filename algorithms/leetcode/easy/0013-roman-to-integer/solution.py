class Solution:
    def romanToInt(self, s: str) -> int:
        """ 羅馬數字轉整數
        
        使用字典儲存羅馬數字對應值，從左到右掃描
        如果當前數字比下一個小，則減去當前值，否則加上當前值
        這是我的解法，時間複雜度 O(n)，空間複雜度 O(1)
        """
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        for i in range(len(s)):
            # 如果下一個比當前大 → 減法規則
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
