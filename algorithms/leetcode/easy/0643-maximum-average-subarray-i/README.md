# 643. Maximum Average Subarray I

**完成日期：** 2026-01-04

## 解法：滑動窗口（我的解法）

### 程式碼
```python
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        total = 0
        max_value = float('-inf')

        for right in range(len(nums)):
            total += nums[right]

            if right - left + 1 == k:
                max_value = max(max_value, total)
                total -= nums[left]
                left += 1

        return max_value / k
```

### 解題思路
- 使用滑動窗口技巧，窗口大小固定為 k
- 遍歷數組時累加元素值
- 當窗口達到大小 k 時，更新最大總和
- 移動窗口：減去左邊元素，加上右邊元素
- 最後將最大總和除以 k 得到最大平均值

## 解法二：優化的滑動窗口（學到的新解法）

### 程式碼
```python
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_values = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_values = max(max_values, window_sum)

        return max_values / k
```

### 解題思路
1. 先計算第一個窗口（前 k 個元素）的總和
2. 從第 k 個元素開始滑動：
   - 減去窗口最左邊的元素（nums[i-k]）
   - 加上新進入窗口的元素（nums[i]）
3. 每次更新最大總和
4. 最後將最大總和除以 k

### 與第一種解法的比較
- **時間複雜度**：都是 O(n)
- **空間複雜度**：都是 O(1)
- **優點**：更簡潔，不需要維護兩個指針
- **學習點**：有時先計算初始狀態會讓邏輯更清晰
