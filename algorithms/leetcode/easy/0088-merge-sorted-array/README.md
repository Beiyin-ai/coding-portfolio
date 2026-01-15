88. Merge Sorted Array
完成日期： 2026-01-15
難度： Easy
標籤： Array, Two Pointers, Sorting
連結： LeetCode 88

## 題目描述
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums2 into nums1 as one sorted array.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

## 範例
**範例 1：**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

**範例 2：**
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

**範例 3：**
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

## 限制條件
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

## 解法：從後向前合併（我的解法）
### 程式碼
```python
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
```

### 解題思路
1. **反向操作**：從兩個陣列的末尾開始比較，避免覆蓋 nums1 中的有效元素
2. **三個指針**：
   - ：指向 nums1 有效部分的最後一個元素
   - ：指向 nums2 的最後一個元素
   - ：指向 nums1 的最後一個位置（存放結果）
3. **比較與放置**：比較 nums1[i] 和 nums2[j]，將較大的放在 nums1[k]
4. **處理剩餘元素**：如果 nums2 有剩餘元素，直接複製到 nums1 前面

## 我的思考過程
1. **問題分析**：需要原地合併兩個已排序陣列，不能使用額外空間
2. **關鍵挑戰**：nums1 前面有有效數據，不能直接從前面開始合併（會覆蓋數據）
3. **靈感來源**：想到可以從後面前操作，利用 nums1 後面的空白位置
4. **設計演算法**：
   - 從最大元素開始處理
   - 每次選擇兩個陣列中較大的元素
   - 放入 nums1 的末尾
5. **邊界條件**：
   - nums1 為空（m=0）：直接複製 nums2
   - nums2 為空（n=0）：不需要操作

## 關鍵點
- **從後向前操作**：這是本題的核心技巧，避免數據覆蓋
- **指針管理**：需要三個指針分別追蹤位置
- **原地操作**：完全符合題目要求的 O(1) 額外空間
- **剩餘元素處理**：只需要處理 nums2 的剩餘元素（因為 nums1 的剩餘元素已經在正確位置）
- **邊界條件**：
  - m=0 或 n=0 的情況
  - 陣列長度為 0 的情況

## 複雜度分析
- **時間複雜度**：O(m + n)
  - 每個元素最多被訪問一次
  - 需要遍歷兩個陣列的所有元素
- **空間複雜度**：O(1)
  - 只使用了常數額外空間（三個指針變數）
  - 完全符合原地操作的要求

## 測試範例
**測試 1**：nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
→ 步驟：
   比較 3 和 6 → 放 6
   比較 3 和 5 → 放 5
   比較 3 和 2 → 放 3
   比較 2 和 2 → 放 2
   比較 1 和 2 → 放 2
   放 1
→ 結果：[1,2,2,3,5,6]

**測試 2**：nums1=[1], m=1, nums2=[], n=0
→ 結果：[1]

**測試 3**：nums1=[0], m=0, nums2=[1], n=1
→ 結果：[1]

**測試 4**：nums1=[4,5,6,0,0,0], m=3, nums2=[1,2,3], n=3
→ 結果：[1,2,3,4,5,6]

**測試 5**：nums1=[1,3,5,0,0], m=3, nums2=[2,4], n=2
→ 結果：[1,2,3,4,5]

## 學習心得
這題讓我學到：
1. **反向思維**：有時候從後面前操作比從前往後更有效率
2. **原地演算法設計**：如何在有限空間內完成複雜操作
3. **指針技巧**：多指針協同工作的設計模式
4. **邊界情況處理**：空陣列、長度為 0 等特殊情況
5. **陣列操作**：如何在不使用額外空間的情況下合併陣列

## 相關題目
- 21. Merge Two Sorted Lists (Easy) - 合併兩個已排序鏈表
- 977. Squares of a Sorted Array (Easy) - 已排序陣列的平方
- 986. Interval List Intersections (Medium) - 區間列表的交集
- 56. Merge Intervals (Medium) - 合併區間

## 下一步計畫
- 嘗試解決 21. Merge Two Sorted Lists
- 練習更多陣列操作相關的題目
- 學習其他合併演算法
