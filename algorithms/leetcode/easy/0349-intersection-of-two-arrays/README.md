349. Intersection of Two Arrays
完成日期： 2026-01-16
難度： Easy
標籤： Array, Hash Table, Two Pointers, Binary Search, Sorting
連結： LeetCode 349

## 題目描述
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

## 範例
**範例 1：**
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

**範例 2：**
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

## 限制條件
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[j] <= 1000

## 解法：使用集合（Hash Set）的解法（我的解法）
### 程式碼
```python
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
```

### 解題思路
1. **去重處理**：將第一個陣列轉為集合，自動去除重複元素
2. **檢查交集**：遍歷第二個陣列，檢查元素是否在集合中
3. **避免重複**：找到交集元素後，從集合中移除，確保結果中每個元素只出現一次
4. **收集結果**：將交集元素加入結果列表

## 我的思考過程
1. **問題分析**：需要找兩個陣列的共同元素，且結果不能有重複
2. **關鍵觀察**：集合（Set）資料結構非常適合這個問題，因為：
   - 集合自動去重
   - 集合的查找操作是 O(1) 時間複雜度
3. **設計演算法**：
   - 用集合儲存第一個陣列的所有唯一元素
   - 遍歷第二個陣列，檢查元素是否在集合中
   - 找到後加入結果，並從集合移除避免重複
4. **時間/空間權衡**：使用額外空間（集合）來換取時間效率

## 關鍵點
- **集合的使用**：Python 的 `set()` 自動去重且提供 O(1) 查找
- **避免重複的策略**：找到交集後立即從集合中移除元素
- **時間效率**：O(n+m) 時間複雜度，比暴力解 O(n*m) 好很多
- **邊界條件**：
  - 空陣列：會返回空列表
  - 沒有交集：返回空列表
  - 陣列長度差異大：依然有效

## 複雜度分析
- **時間複雜度**：O(n + m)
  - 建立集合：O(n)，其中 n 是 nums1 的長度
  - 遍歷 nums2：O(m)，其中 m 是 nums2 的長度
  - 集合查找和移除：O(1)
- **空間複雜度**：O(n)
  - 最壞情況下需要儲存 nums1 的所有唯一元素
  - 結果列表：O(k)，其中 k 是交集元素數量

## 測試範例
**測試 1**：nums1=[1,2,2,1], nums2=[2,2]
→ set1 = {1,2}
→ 檢查 nums2：2 在 set1 中，加入結果，移除 2
→ set1 = {1}
→ 檢查下一個 2：不在 set1 中
→ 結果：[2]

**測試 2**：nums1=[4,9,5], nums2=[9,4,9,8,4]
→ set1 = {4,9,5}
→ 檢查 nums2：9 在 set1 中，加入結果，移除 9
→ 4 在 set1 中，加入結果，移除 4
→ 9 不在 set1 中
→ 8 不在 set1 中
→ 4 不在 set1 中
→ 結果：[9,4] 或 [4,9]

**測試 3**：nums1=[1,2,3], nums2=[4,5,6]
→ 沒有交集，返回 []

**測試 4**：nums1=[], nums2=[1,2,3]
→ set1 = {}，返回 []

**測試 5**：nums1=[1,1,1], nums2=[1,1,1]
→ 結果：[1]

## 學習心得
這題讓我學到：
1. **集合的應用**：當需要去重或快速查找時，集合是很好的選擇
2. **時間空間的權衡**：用額外空間換取時間效率的常見模式
3. **交集問題的模式**：先將一個集合轉為哈希表，再檢查另一個集合
4. **避免重複的技巧**：找到元素後立即從集合中移除
5. **Python 集合操作**：Python 也支援集合的內建交集操作 `set1 & set2`

## 相關題目
- 350. Intersection of Two Arrays II (Easy) - 這題的進階版，需要保留重複次數
- 242. Valid Anagram (Easy) - 同樣使用哈希表解決的問題
- 202. Happy Number (Easy) - 使用集合檢測循環
- 217. Contains Duplicate (Easy) - 檢查重複元素

## 下一步計畫
- 嘗試解決 350. Intersection of Two Arrays II
- 學習使用 Python 內建的集合運算符
- 練習更多哈希表相關的題目
