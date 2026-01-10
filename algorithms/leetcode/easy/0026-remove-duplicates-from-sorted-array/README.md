26. Remove Duplicates from Sorted Array
完成日期： 2026-01-10
難度： Easy
標籤： Array, Two Pointers
連結： LeetCode 26

## 題目描述
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

**Custom Judge:**
The judge will test your solution with the following code:
```java
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.

## 範例
**範例 1：**
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

**範例 2：**
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

## 限制條件
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.

## 解法：雙指針法（我的解法）
### 程式碼
```python
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
```

### 解題思路
1. **使用雙指針技巧**：
   - 指針 ：指向當前已處理的唯一元素的最後位置
   - 指針 ：遍歷整個陣列
2. **核心邏輯**：當  與  不同時，表示找到新的唯一元素
3. **原地修改**：將新找到的唯一元素放到  的位置
4. **返回結果**：最後  就是唯一元素的數量

## 我的思考過程
1. **問題分析**：需要原地修改陣列，不能使用額外空間
2. **觀察特性**：陣列已排序，重複元素會相鄰出現
3. **靈感來源**：想到雙指針技巧很適合處理這種
4. **設計演算法**：
   - 從第二個元素開始遍歷
   - 比較當前元素與前一個唯一元素
   - 不同時移動指針並更新值

## 關鍵點
- **雙指針技巧**：這是處理陣列原地修改的常用技巧
- **邊界條件**：
  - 空陣列：直接返回 0
  - 只有一個元素：直接返回 1
- **原地操作**：不能使用額外陣列，必須修改原陣列
- **返回值的意義**：返回的是唯一元素的數量，不是陣列長度

## 複雜度分析
- **時間複雜度**：O(n)
  - 只需要遍歷陣列一次
  - 每個元素最多被訪問一次
- **空間複雜度**：O(1)
  - 只使用了常數額外空間（兩個指針變數）
  - 完全符合題目要求的原地修改

## 測試範例
**測試 1**：[1,1,2]
→ 返回 2，陣列變為 [1,2,2]

**測試 2**：[0,0,1,1,1,2,2,3,3,4]
→ 返回 5，陣列變為 [0,1,2,3,4,2,2,3,3,4]

**測試 3**：[]
→ 返回 0

**測試 4**：[1]
→ 返回 1

**測試 5**：[1,2,3,4,5]
→ 返回 5

## 學習心得
這題讓我學到：
1. **雙指針技巧**：非常適合處理已排序陣列的問題
2. **原地演算法**：如何在不使用額外空間的情況下修改陣列
3. **邊界條件處理**：空陣列、單元素陣列等特殊情況
4. **解題模式**：已排序陣列 + 移除重複 → 考慮雙指針

## 相關題目
- 27. Remove Element (Easy) - 類似概念，移除特定值
- 80. Remove Duplicates from Sorted Array II (Medium) - 這題的進階版，允許最多兩個重複
- 283. Move Zeroes (Easy) - 也是雙指針的應用

## 下一步計畫
- 嘗試解決 80. Remove Duplicates from Sorted Array II
- 練習更多雙指針相關的題目
- 學習其他陣列處理技巧
