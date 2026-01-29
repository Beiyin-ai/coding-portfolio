21. Merge Two Sorted Lists
完成日期： 2026-01-29
難度： Easy
標籤： Linked List, Recursion
連結： LeetCode 21

## 題目描述
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## 範例
**範例 1：**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**範例 2：**
```
Input: list1 = [], list2 = []
Output: []
```

**範例 3：**
```
Input: list1 = [], list2 = [0]
Output: [0]
```

## 限制條件
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

## 解法：迭代法（我的解法）
### 程式碼
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ 合併兩個有序鏈表

        使用虛擬頭節點技巧，迭代比較兩個鏈表的節點
        這是我的解法，清晰且高效
        """
        dummy = ListNode(-1)  # 創建虛擬頭節點
        current = dummy

        # 比較兩個鏈表的當前節點，選擇較小的加入結果鏈表
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        # 將剩餘的部分鏈接起來
        current.next = list1 if list1 else list2

        return dummy.next  # 返回真正的頭節點
```

### 解題思路
1. **創建虛擬頭節點**：`dummy = ListNode(-1)`，簡化邊界條件處理
2. **初始化指針**：`current` 指向當前結果鏈表的末尾
3. **迭代比較**：比較兩個鏈表的當前節點值，將較小的節點連接到結果鏈表
4. **移動指針**：將對應鏈表的指針向後移動，同時移動 `current` 指針
5. **處理剩餘部分**：當一個鏈表為空時，將另一個鏈表的剩餘部分直接連接
6. **返回結果**：返回 `dummy.next`，即合併後鏈表的真正頭節點

### 複雜度分析
- **時間複雜度**：O(n + m)
  - 需要遍歷兩個鏈表的所有節點
  - n 是 list1 的長度，m 是 list2 的長度
- **空間複雜度**：O(1)
  - 只使用了常數級別的額外空間
  - 沒有創建新節點，只是重新連接現有節點

## 我的思考過程
### 第一階段：理解問題
1. **問題類型**：這是鏈表操作的基本問題，合併兩個已排序的鏈表
2. **關鍵要求**：必須在原鏈表上操作，不能創建新節點（題目說 "splicing together"）
3. **邊界條件**：考慮空鏈表的情況

### 第二階段：設計解法
1. **虛擬頭節點技巧**：為了避免處理頭節點的特殊情況
2. **雙指針迭代**：使用兩個指針分別遍歷兩個鏈表
3. **比較與連接**：比較當前節點值，連接較小的節點
4. **處理剩餘**：當一個鏈表遍歷完後，直接連接另一個鏈表的剩餘部分

### 第三階段：實現細節
1. **初始化**：創建 dummy 節點和 current 指針
2. **循環條件**：`while list1 and list2:` 確保兩個鏈表都還有節點
3. **比較邏輯**：使用 `if list1.val > list2.val:` 比較節點值
4. **指針移動**：每次連接後都要移動對應的鏈表指針
5. **邊界處理**：使用三元運算子處理剩餘部分

## 關鍵點
### 1. 虛擬頭節點（Dummy Node）技巧
- **目的**：簡化代碼，避免處理頭節點的特殊情況
- **創建**：`dummy = ListNode(-1)`
- **返回**：`return dummy.next`

### 2. 指針操作
- **current 指針**：指向結果鏈表的當前末尾
- **list1/list2 指針**：分別指向兩個輸入鏈表的當前節點
- **節點連接**：`current.next = list1` 或 `current.next = list2`

### 3. 邊界條件處理
- **空鏈表**：如果一個鏈表為空，直接返回另一個鏈表
- **剩餘部分**：`current.next = list1 if list1 else list2`
- **循環結束**：當一個鏈表為空時結束循環

## 測試範例
### 測試 1：正常情況
- list1 = [1,2,4], list2 = [1,3,4]
- 合併過程：
  1. 比較 1 和 1 → 連接 list1 的 1
  2. 比較 2 和 1 → 連接 list2 的 1
  3. 比較 2 和 3 → 連接 list1 的 2
  4. 比較 4 和 3 → 連接 list2 的 3
  5. 比較 4 和 4 → 連接 list1 的 4
  6. list1 結束，連接 list2 剩餘的 4
- 結果：[1,1,2,3,4,4]

### 測試 2：兩個空鏈表
- list1 = [], list2 = []
- 直接返回 `dummy.next`，即 `None`
- 結果：[]

### 測試 3：一個空鏈表
- list1 = [], list2 = [0]
- `while` 循環不執行
- `current.next = list2`（因為 list1 為空）
- 結果：[0]

### 測試 4：鏈表長度不同
- list1 = [1,3,5], list2 = [2,4]
- 結果：[1,2,3,4,5]

## 學習心得
這題讓我學到：
1. **虛擬頭節點技巧**：簡化鏈表操作，避免特殊情況處理
2. **鏈表指針操作**：理解指針的移動和節點的連接
3. **迭代思維**：使用循環逐步構建結果鏈表
4. **空間優化**：在原有節點上操作，不需要額外空間
5. **邊界條件**：處理空鏈表和剩餘部分的重要性

## 相關題目
- **23. Merge k Sorted Lists** (Hard) - 合併多個有序鏈表
- **88. Merge Sorted Array** (Easy) - 合併兩個有序數組
- **148. Sort List** (Medium) - 鏈表排序
- **206. Reverse Linked List** (Easy) - 反轉鏈表
- **160. Intersection of Two Linked Lists** (Easy) - 鏈表相交

## 下一步計畫
1. 嘗試 **206. Reverse Linked List**（鏈表反轉）
2. 練習更多鏈表相關的題目
3. 學習遞迴解法來解決鏈表問題
