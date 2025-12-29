"""
LeetCode 217. Contains Duplicate
"""

from typing import List

class Solution:
    def containsDuplicate_bruteforce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    def containsDuplicate_set(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.containsDuplicate_set(nums)

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
    ]
    
    print("=== Contains Duplicate 測試 ===")
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result1 = solution.containsDuplicate_bruteforce(nums)
        result2 = solution.containsDuplicate_set(nums)
        
        status1 = "✓" if result1 == expected else "✗"
        status2 = "✓" if result2 == expected else "✗"
        
        print(f"測試 {i}: {status1}{status2}")
        print(f"  輸入: {nums}")
        print(f"  預期: {expected}")
        print(f"  暴力法: {result1}")
        print(f"  Set法: {result2}")
        print()
