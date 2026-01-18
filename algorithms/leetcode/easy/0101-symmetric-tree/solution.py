from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """ 檢查二元樹是否對稱
        
        使用遞迴方法比較樹的左右子樹是否互為鏡像
        這是我的解法，清晰直觀
        """
        if not root:
            return True

        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            """ 檢查兩棵樹是否互為鏡像 """
            # 兩棵樹都為空，對稱
            if not t1 and not t2:
                return True
            # 只有一棵樹為空，不對稱
            if not t1 or not t2:
                return False
            # 當前節點值相等，且左子樹與右子樹鏡像，右子樹與左子樹鏡像
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)
