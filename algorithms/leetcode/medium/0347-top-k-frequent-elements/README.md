# 347. Top K Frequent Elements

**難度：** Medium  
**標籤：** Array, Hash Table, Divide and Conquer, Sorting, Heap, Bucket Sort  
**連結：** [LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)

## 題目描述
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### 範例
**範例 1：**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**範例 2：**
```
Input: nums = [1], k = 1
Output: [1]
```

**範例 3：**
```
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
```

### 限制條件
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

### Follow up
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## 解法：使用 Counter.most_common()（我的解法）

### 程式碼
```python
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = Counter(nums)
        most_common_nums = dict_nums.most_common(k)
        result = []
        for items in most_common_nums:
            result.append(items[0])
        return result
```

### 解題思路
1. **統計頻率**：使用 `Counter` 統計每個數字出現的次數
2. **取得前 k 個**：使用 `most_common(k)` 方法直接取得出現頻率最高的 k 個元素
3. **提取結果**：從 `(數字, 頻率)` 元組中提取數字部分

### 我的思考過程
我想到這題需要統計頻率，所以自然想到用 `Counter`
然後需要取前 k 個最高頻率的，`Counter` 正好有 `most_common()` 方法
這樣程式碼非常簡潔，直接利用 Python 內建功能

### 關鍵點
- **Counter 的使用**：Python 中統計頻率最方便的工具
- **most_common() 方法**：直接解決「取前 k 個」的需求
- **時間複雜度**：`most_common()` 使用 heap，時間複雜度為 O(n log k)，符合要求

### 複雜度分析
- **時間複雜度：O(n log k)**
  - `Counter(nums)`：O(n) 遍歷一次陣列
  - `most_common(k)`：使用 heap，O(n log k)
  - 總體：O(n + n log k) = O(n log k)，優於 O(n log n)
- **空間複雜度：O(n)**
  - `Counter` 儲存所有獨特數字及其頻率

### 測試範例
```python
測試 1: nums = [1,1,1,2,2,3], k = 2
→ [1, 2]

測試 2: nums = [1], k = 1
→ [1]

測試 3: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
→ [1, 2]

測試 4: nums = [4,1,-1,2,-1,2,3], k = 2
→ [-1, 2]
```

### 學習心得
這題讓我學習到：
1. **善用內建函式**：Python 的 `Counter` 和 `most_common()` 非常強大
2. **時間複雜度考慮**：題目要求優於 O(n log n)，需要選擇合適的演算法
3. **從簡單開始**：先用最簡單的方法解決，再考慮優化

這是我的第二個 Medium 題目，讓我更熟悉頻率統計相關的問題！

### 相關題目
- [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) (Medium)
- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium)
- [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) (Medium)

### 下一步計畫
1. 嘗試用 Heap 或 Bucket Sort 實現
2. 練習相關的 Top K 問題
3. 學習更多排序和堆積的應用
