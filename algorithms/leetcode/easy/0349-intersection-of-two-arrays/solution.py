from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 尋找兩個陣列的交集
        
        使用集合來儲存第一個陣列的唯一元素
        然後檢查第二個陣列中的元素是否在集合中
        這是我的解法，時間複雜度 O(n+m)，空間複雜度 O(n)
        """
        result = []
        set1 = set(nums1)  # 將 nums1 轉為集合去重

        for num in nums2:
            if num in set1:
                result.append(num)
                set1.remove(num)  # 避免重複加入

        return result
