"""
21. Merge Two Sorted Lists - 其他解法
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """遞迴解法"""
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1.val < list2.val:
        list1.next = mergeTwoLists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists_recursive(list1, list2.next)
        return list2

def mergeTwoLists_inplace(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """不使用虛擬節點的原地解法"""
    if not list1:
        return list2
    if not list2:
        return list1
    
    # 確定頭節點
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    
    current = head
    
    # 合併剩餘部分
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # 連接剩餘部分
    current.next = list1 if list1 else list2
    
    return head

def mergeTwoLists_simple(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """簡化版虛擬頭節點解法"""
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    tail.next = list1 or list2
    return dummy.next

# 比較所有解法
def create_linked_list(values):
    """創建鏈表"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """將鏈表轉換為列表"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0]),
        ([1, 3, 5], [2, 4]),
    ]
    
    solutions = [
        ("原始迭代法", Solution().mergeTwoLists),
        ("遞迴解法", mergeTwoLists_recursive),
        ("原地解法", mergeTwoLists_inplace),
        ("簡化版", mergeTwoLists_simple),
    ]
    
    print("不同解法的比較：")
    print("=" * 60)
    
    for list1_vals, list2_vals in test_cases:
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        
        print(f"\n測試案例: list1={list1_vals}, list2={list2_vals}")
        
        # 為每個解法創建新的鏈表（因為解法會修改原鏈表）
        for name, func in solutions:
            list1_copy = create_linked_list(list1_vals)
            list2_copy = create_linked_list(list2_vals)
            result = func(list1_copy, list2_copy)
            result_list = linked_list_to_list(result)
            print(f"  {name:15}: {result_list}")
