from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        找出最富有的客戶財富總和

        新解法：使用生成器表達式和 max 函數
        更簡潔，一行解決
        """
        return max(sum(customer) for customer in accounts)
