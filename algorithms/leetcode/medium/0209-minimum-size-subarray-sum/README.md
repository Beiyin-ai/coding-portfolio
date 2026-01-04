# 209. Minimum Size Subarray Sum

**完成日期：** 2026-01-04

**難度：** Medium
**標籤：** Array, Sliding Window, Two Pointers, Binary Search, Prefix Sum
**連結：** [LeetCode 209](https://leetcode.com/problems/minimum-size-subarray-sum/)

## 題目描述
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

### 範例
**範例 1：**
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**範例 2：**
```
Input: target = 4, nums = [1,4,4]
Output: 1
```

**範例 3：**
```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

### 限制條件
- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## 解法：滑動窗口（我的解法）

### 程式碼
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len
```

### 解題思路
1. **使用滑動窗口**：用兩個指針 `left` 和 `right` 定義當前子數組
2. **擴大窗口**：`right` 指針向右移動，累加元素值
3. **收縮窗口**：當總和 ≥ target 時，更新最小長度，並移動 `left` 縮小窗口
4. **持續遍歷**：直到 `right` 遍歷完整個數組

### 我的思考過程
我想到這題要求連續子數組，很適合用滑動窗口來解決。
因為數組都是正整數，當窗口擴大時總和增加，窗口縮小時總和減少，這個特性讓滑動窗口非常有效。
我需要記錄當前最小長度，並在找到滿足條件的窗口時更新它。

### 關鍵點
- **滑動窗口**：利用兩個指針動態調整窗口大小
- **正整數保證**：因為都是正整數，窗口縮小時總和一定減少
- **最小長度追蹤**：使用 `float("inf")` 作為初始最大值
- **邊界條件**：當沒有滿足條件的子數組時返回 0

### 複雜度分析
- **時間複雜度：O(n)**
  - 每個元素最多被訪問兩次（`right` 指針一次，`left` 指針一次）
- **空間複雜度：O(1)**
  - 只使用了常數額外空間（幾個變數）

### 測試範例
```python
測試 1: target = 7, nums = [2,3,1,2,4,3]
→ 2 (子數組 [4,3])

測試 2: target = 4, nums = [1,4,4]
→ 1 (子數組 [4])

測試 3: target = 11, nums = [1,1,1,1,1,1,1,1]
→ 0 (沒有滿足條件的子數組)

測試 4: target = 5, nums = [1,2,3,4,5]
→ 1 (子數組 [5])
```

### 學習心得
這題讓我更熟悉滑動窗口技巧。我學到：
1. **滑動窗口的應用時機**：需要找連續子數組且滿足某些條件時
2. **雙指針的協調**：`right` 負責擴大窗口，`left` 負責收縮窗口
3. **正整數的優勢**：數組元素為正數時，滑動窗口的效率最高
4. **邊界條件處理**：記得處理找不到解的情況

### 相關題目
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium) - 我已經解過這題
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard)
- [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) (Medium)

### 下一步計畫
1. 練習更多滑動窗口的變形題
2. 嘗試用前綴和 + 二分搜尋解決這題
3. 挑戰 Hard 難度的滑動窗口題目
