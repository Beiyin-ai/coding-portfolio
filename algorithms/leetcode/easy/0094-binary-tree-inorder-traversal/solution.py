# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ 二元樹中序遍歷
        
        使用遞迴方法實現中序遍歷：左子樹 → 根節點 → 右子樹
        這是我的解法，簡單直觀
        """
        result = []
        if not root:
            return result
        
        # 遞迴實現：左子樹 + 根節點 + 右子樹
        return (self.inorderTraversal(root.left) + 
                [root.val] + 
                self.inorderTraversal(root.right))
