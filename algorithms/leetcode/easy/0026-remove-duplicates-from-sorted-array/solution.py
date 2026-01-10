from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ 移除已排序陣列中的重複元素
        
        使用雙指針技巧：
        - i 指向最後一個唯一元素的位置
        - j 遍歷整個陣列
        這是我的解法，時間複雜度 O(n)，空間複雜度 O(1)
        """
        if not nums:
            return 0
        
        i = 0
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1
