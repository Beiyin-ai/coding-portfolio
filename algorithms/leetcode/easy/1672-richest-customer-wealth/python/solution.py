# 1672. Richest Customer Wealth
# 解題日期: 13天前

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for items in accounts:
            current = 0
            for nums in items:
                current += nums
                if current > richest:
                    richest = current
        return richest
