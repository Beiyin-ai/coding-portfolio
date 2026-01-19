104. Maximum Depth of Binary Tree
完成日期： 2026-01-19
難度： Easy
標籤： Tree, Depth-First Search, Breadth-First Search, Binary Tree
連結： LeetCode 104

## 題目描述
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## 範例
**範例 1：**
Input: root = [3,9,20,null,null,15,7]
Output: 3

**範例 2：**
Input: root = [1,null,2]
Output: 2

## 限制條件
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100

## 解法：遞迴法（我的解法）
### 程式碼
```python
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
```

### 解題思路
1. **遞迴定義**：一棵樹的最大深度等於 1 加上其左右子樹的最大深度
2. **終止條件**：當節點為空時，深度為 0
3. **遞迴計算**：
   - 計算左子樹的最大深度
   - 計算右子樹的最大深度
   - 取兩者中的最大值，再加 1（當前節點）
4. **返回結果**：返回計算出的最大深度

## 我的思考過程
1. **問題分析**：需要找出從根節點到最遠葉節點的路徑長度
2. **關鍵觀察**：樹的深度問題天然適合遞迴解決
3. **設計遞迴**：
   - 空樹深度為 0
   - 非空樹深度 = 1 + max(左子樹深度, 右子樹深度)
4. **實現細節**：
   - 使用 `max()` 函數取最大值
   - 注意 Python 中空節點的判斷 `if not root:`
5. **時間/空間考量**：遞迴解法簡潔，時間複雜度 O(n)

## 關鍵點
- **遞迴關係**：depth(node) = 1 + max(depth(left), depth(right))
- **終止條件**：空節點的深度為 0
- **樹的深度定義**：從根節點到最遠葉節點的節點數量（包括根節點）
- **葉節點處理**：葉節點的左右子樹都為空，深度為 1
- **邊界條件**：
  - 空樹：返回 0
  - 只有根節點：返回 1
  - 不平衡的樹：依然正確計算

## 複雜度分析
- **時間複雜度**：O(n)
  - 每個節點只被訪問一次
  - n 是樹中節點的數量
- **空間複雜度**：O(n)
  - 遞迴調用棧深度：最壞情況 O(n)（當樹退化為鏈表時）
  - 平均情況 O(log n)（平衡樹時）

## 測試範例
**測試 1**：root = [3,9,20,null,null,15,7]
→ 樹結構：
       3
     /   \
    9     20
         /  \
        15   7
→ 計算過程：
  depth(9) = 1
  depth(20) = 1 + max(depth(15), depth(7)) = 1 + 1 = 2
  depth(3) = 1 + max(1, 2) = 3
→ 結果：3

**測試 2**：root = [1,null,2]
→ 樹結構：
    1
     \
      2
→ 計算過程：
  depth(2) = 1
  depth(1) = 1 + max(0, 1) = 2
→ 結果：2

**測試 3**：root = []
→ 空樹，返回 0

**測試 4**：root = [1]
→ 只有根節點，返回 1

**測試 5**：root = [1,2,3,4,5,6,7]
→ 完全二元樹，深度計算
→ 結果：3

## 學習心得
這題讓我學到：
1. **樹的深度計算**：經典的遞迴問題，理解遞迴關係是關鍵
2. **遞迴的基礎應用**：如何將問題分解為子問題
3. **最大深度的定義**：從根節點到最遠葉節點的節點數量
4. **Python 的 max() 函數**：簡化代碼，提高可讀性
5. **樹問題的模式**：許多樹問題都可以用類似的遞迴框架解決

## 相關題目
- 110. Balanced Binary Tree (Easy) - 檢查樹是否平衡
- 111. Minimum Depth of Binary Tree (Easy) - 最小深度
- 543. Diameter of Binary Tree (Easy) - 樹的直徑
- 559. Maximum Depth of N-ary Tree (Easy) - N叉樹的最大深度

## 下一步計畫
- 嘗試解決 110. Balanced Binary Tree
- 練習迭代解法（使用層序遍歷 BFS）
- 學習更多樹的變形問題
