"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """ 深度拷貝圖
        
        使用 DFS 遞迴遍歷，並用 HashMap 避免重複複製
        這是我的解法，清晰易懂
        """
        if not node:
            return None
        
        clone = {}
        
        def DFS(curr):
            if curr in clone: 
                return clone[curr]
            
            clone[curr] = Node(curr.val)
            
            for nei in curr.neighbors:
                clone[curr].neighbors.append(DFS(nei))
            
            return clone[curr]
        
        return DFS(node)
