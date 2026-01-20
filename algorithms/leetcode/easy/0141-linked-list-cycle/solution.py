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
