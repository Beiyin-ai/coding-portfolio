from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ 合併兩個已排序陣列
        
        從陣列末尾開始比較，避免覆蓋 nums1 的有效元素
        這是我的解法，時間複雜度 O(m+n)，空間複雜度 O(1)
        """
        i = m - 1  # nums1 有效部分的最後一個索引
        j = n - 1  # nums2 的最後一個索引
        k = m + n - 1  # nums1 的最後一格索引

        # 從後向前比較並合併
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # 如果 nums2 還有剩餘元素，補到 nums1 前面
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
