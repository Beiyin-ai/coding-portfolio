# 1672. Richest Customer Wealth

from typing import List

class Solution:
    def maximumWealth_naive(self, accounts: List[List[int]]) -> int:
        """基本解法：雙層迴圈"""
        richest = 0
        for items in accounts:
            current = 0
            for nums in items:
                current += nums
                if current > richest:
                    richest = current
        return richest

    def maximumWealth_sum(self, accounts: List[List[int]]) -> int:
        """使用 sum() 函數簡化"""
        richest = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > richest:
                richest = wealth
        return richest

    def maximumWealth_oneliner(self, accounts: List[List[int]]) -> int:
        """一行解法：max + 列表推導式"""
        return max(sum(customer) for customer in accounts)

    # LeetCode 要求的方法
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return self.maximumWealth_oneliner(accounts)

# 測試程式碼
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [[1,2,3],[3,2,1]],
        [[1,5],[7,3],[3,5]],
        [[2,8,7],[7,1,3],[1,9,5]]
    ]

    print("=== Richest Customer Wealth 測試 ===")
    for accounts in test_cases:
        result1 = solution.maximumWealth_naive(accounts)
        result2 = solution.maximumWealth_sum(accounts)
        result3 = solution.maximumWealth_oneliner(accounts)

        print(f"輸入: {accounts}")
        print(f"基本法: {result1}")
        print(f"sum法:  {result2}")
        print(f"一行法: {result3}")
        print(f"結果相同: {result1 == result2 == result3}")
        print()
