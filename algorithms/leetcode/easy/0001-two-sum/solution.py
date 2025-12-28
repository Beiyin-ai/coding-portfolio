"""
LeetCode 1. Two Sum

解法 1：暴力法（我的第一個解法）
時間複雜度：O(n²)
空間複雜度：O(1)

解題歷程：
這是我解 LeetCode 的第一題，從最基礎的暴力解法開始。
學習策略：先寫出能工作的解法，再逐步優化。
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        暴力解法：雙重迴圈檢查所有組合
        
        思路：
        1. 第一層迴圈選定第一個數
        2. 第二層迴圈從下一個位置開始選第二個數
        3. 檢查兩數之和是否等於 target
        
        這是我的第一個解法，雖然效率不高但容易理解。
        未來會學習更優化的 HashMap 解法。
        """
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []  # 題目保證有解，這行通常不會執行


# 測試程式碼
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    print("=== Two Sum 測試 ===")
    print(f"解法：暴力雙重迴圈\n")
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.twoSum(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"測試 {i}: {status}")
        print(f"  輸入: nums = {nums}, target = {target}")
        print(f"  預期: {expected}")
        print(f"  結果: {result}")
        print()
