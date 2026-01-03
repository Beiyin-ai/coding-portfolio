# 1480. Running Sum of 1d Array

**完成日期：** 2025-12-26  

## 問題描述
給定一個整數陣列 nums，返回其累加和陣列。
累加和陣列的每個元素 output[i] = sum(nums[0]...nums[i])

## 解法

### 程式碼
```python
from typing import List

class Solution:
    def runningSum_basic(self, nums: List[int]) -> List[int]:
        output = 0
        outputList = []
        for num in nums:
            output += num
            outputList.append(output)
        return outputList

    def runningSum_inplace(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
```

### 解題思路
**解法1：基本累加**
1. 初始化累加變數 output = 0
2. 初始化結果列表 outputList = []
3. 遍歷 nums 中的每個數字：
   - 將當前數字加到 output
   - 將 output 添加到 outputList

**解法2：原地修改**
1. 從第二個元素開始遍歷陣列
2. 每個元素等於自己加上前一個元素
3. 直接修改原陣列，節省空間

### 複雜度分析
- **時間複雜度：O(n)**，需要遍歷陣列一次
- **空間複雜度：**
  - 基本法：O(n)，需要額外陣列
  - 原地法：O(1)，只使用常數空間

## 測試結果
所有測試案例都通過！✓
