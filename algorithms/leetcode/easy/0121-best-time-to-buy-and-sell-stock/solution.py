from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        買賣股票的最佳時機（只能交易一次）
        
        解法2：使用 min/max 函數，更簡潔
        時間複雜度：O(n)
        空間複雜度：O(1)
        """
        min_price = float("inf")  # 初始化最小價格為無窮大
        max_profit = 0           # 初始化最大利潤為0
        
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
                
        return max_profit
