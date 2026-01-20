141. Linked List Cycle
完成日期： 2026-01-20
難度： Easy
標籤： Hash Table, Linked List, Two Pointers
連結： LeetCode 141

## 題目描述
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## 範例
**範例 1：**
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**範例 2：**
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

**範例 3：**
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

## 限制條件
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

## 解法：Floyd's Cycle-Finding Algorithm (龜兔賽跑算法)（我的解法）
### 程式碼
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ 檢測鏈表是否有環
        
        使用快慢指針（龜兔賽跑算法）：
        - 慢指針每次走一步
        - 快指針每次走兩步
        - 如果有環，快慢指針最終會相遇
        這是我的解法，時間複雜度 O(n)，空間複雜度 O(1)
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next        # 慢走一步
            fast = fast.next.next   # 快走兩步

            if slow == fast:        # 相遇 → 有環
                return True

        return False                # 快指標走到 None → 沒環
```

### 解題思路
1. **快慢指針初始化**：都從頭節點開始
2. **循環移動**：
   - 慢指針每次移動一步
   - 快指針每次移動兩步
3. **檢測相遇**：如果快慢指針指向同一個節點，表示有環
4. **檢測終止**：如果快指針或快指針的下一個節點為 None，表示無環
5. **數學原理**：在有環的情況下，快指針最終會追上慢指針

## 我的思考過程
1. **問題分析**：需要檢測鏈表中是否存在循環
2. **解決方案選擇**：
   - 方案一：使用哈希表記錄訪問過的節點，空間複雜度 O(n)
   - 方案二：使用快慢指針（Floyd 算法），空間複雜度 O(1)
3. **選擇快慢指針的原因**：
   - 空間效率更好
   - 經典算法，面試常考
   - 邏輯清晰，實現簡單
4. **實現細節**：
   - 注意邊界條件：空鏈表、單節點鏈表
   - 循環條件：`while fast and fast.next:` 確保快指針可以安全移動兩步
   - 初始條件：快慢指針都從 head 開始

## 關鍵點
- **Floyd 算法**：也稱為龜兔賽跑算法，是檢測循環的經典方法
- **指針移動速度**：慢指針一步，快指針兩步
- **相遇條件**：快慢指針指向同一個節點表示有環
- **終止條件**：快指針遇到 None 表示無環
- **時間複雜度**：O(n)，最壞情況需要遍歷整個鏈表
- **空間複雜度**：O(1)，只使用兩個指針

## 複雜度分析
- **時間複雜度**：O(n)
  - 無環情況：快指針會先到達末尾，訪問約 n/2 個節點
  - 有環情況：慢指針走完整個環之前，快指針會追上慢指針
  - 最壞情況：O(n+k)，其中 k 是環的長度
- **空間複雜度**：O(1)
  - 只使用了兩個指針變數
  - 不需要額外數據結構

## 測試範例
**測試 1**：head = [3,2,0,-4], pos = 1
→ 鏈表結構：3 → 2 → 0 → -4 → 2 (形成環)
→ 快慢指針移動：
  初始：slow=3, fast=3
  第一步：slow=2, fast=0
  第二步：slow=0, fast=2
  第三步：slow=-4, fast=-4 (相遇)
→ 結果：True

**測試 2**：head = [1,2], pos = 0
→ 鏈表結構：1 → 2 → 1 (形成環)
→ 快慢指針移動：
  初始：slow=1, fast=1
  第一步：slow=2, fast=2 (相遇)
→ 結果：True

**測試 3**：head = [1], pos = -1
→ 鏈表結構：1 → None
→ 快慢指針移動：
  初始：slow=1, fast=1
  第一步：fast=None，循環終止
→ 結果：False

**測試 4**：head = []
→ 空鏈表，fast=None，循環不執行
→ 結果：False

**測試 5**：head = [1,2,3,4,5], pos = -1
→ 無環鏈表，最終 fast 會到 None
→ 結果：False

## 學習心得
這題讓我學到：
1. **Floyd 循環檢測算法**：經典的快慢指針技巧
2. **鏈表操作**：如何安全地遍歷鏈表，避免空指針錯誤
3. **時間空間的權衡**：哈希表解法 vs 快慢指針解法
4. **數學思維**：理解為什麼快指針速度是慢指針兩倍時一定會相遇
5. **面試常見題型**：鏈表循環檢測是常見的面試問題

## 相關題目
- 142. Linked List Cycle II (Medium) - 找出循環的起始點
- 202. Happy Number (Easy) - 同樣使用快慢指檢測循環
- 287. Find the Duplicate Number (Medium) - 快慢指針的變形應用
- 876. Middle of the Linked List (Easy) - 快慢指針找中點

## 下一步計畫
- 嘗試解決 142. Linked List Cycle II (找出環的起點)
- 練習 876. Middle of the Linked List (快慢指針找中點)
- 學習更多鏈表相關的算法
