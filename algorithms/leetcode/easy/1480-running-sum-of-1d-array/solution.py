# 1480. Running Sum of 1d Array

from typing import List

class Solution:
    def runningSum_basic(self, nums: List[int]) -> List[int]:
        """基本累加解法"""
        output = 0
        outputList = []
        for num in nums:
            output += num
            outputList.append(output)
        return outputList

    def runningSum_inplace(self, nums: List[int]) -> List[int]:
        """原地修改解法（節省空間）"""
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

    # LeetCode 要求的方法
    def runningSum(self, nums: List[int]) -> List[int]:
        return self.runningSum_basic(nums)

# 測試程式碼
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3, 4],
        [1, 1, 1, 1, 1],
        [3, 1, 2, 10, 1]
    ]

    print("=== Running Sum 測試 ===")
    for nums in test_cases:
        # 複製一份給原地修改用
        nums_copy = nums.copy()
        
        result1 = solution.runningSum_basic(nums)
        result2 = solution.runningSum_inplace(nums_copy)
        
        print(f"輸入: {nums}")
        print(f"基本法: {result1}")
        print(f"原地法: {result2}")
        print(f"結果相同: {result1 == result2}")
        print()
