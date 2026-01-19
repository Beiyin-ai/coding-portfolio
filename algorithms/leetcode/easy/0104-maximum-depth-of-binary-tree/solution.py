# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ 計算二元樹的最大深度
        
        使用遞迴方法，最大深度 = 1 + max(左子樹深度, 右子樹深度)
        這是我的解法，簡潔優雅
        """
        if not root:
            return 0
        
        # 遞迴計算左右子樹的深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 當前節點的深度 = 1 + 左右子樹深度的最大值
        return 1 + max(left_depth, right_depth)
