from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


# 測試程式碼
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
    solution = Solution()
    
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1, 3, 5], [2, 4], [1, 2, 3, 4, 5]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [1, 2, 3], [1, 2, 3]),
    ]
    
    print("Merge Two Sorted Lists 測試結果：")
    print("=" * 60)
    
    all_passed = True
    for i, (list1_vals, list2_vals, expected) in enumerate(test_cases, 1):
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        
        result_head = solution.mergeTwoLists(list1, list2)
        result = linked_list_to_list(result_head)
        
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        
        print(f"測試 {i}:")
        print(f"  list1: {list1_vals}")
        print(f"  list2: {list2_vals}")
        print(f"  結果: {result} {status} (預期: {expected})")
        print()
    
    print("=" * 60)
    if all_passed:
        print("✅ 所有測試通過！")
    else:
        print("❌ 有測試失敗！")
    
    # 詳細演示一個案例
    print("\n詳細演示（範例1）：")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    print(f"合併前 list1: {linked_list_to_list(list1)}")
    print(f"合併前 list2: {linked_list_to_list(list2)}")
    
    merged = solution.mergeTwoLists(list1, list2)
    print(f"合併後: {linked_list_to_list(merged)}")
