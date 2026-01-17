94. Binary Tree Inorder Traversal
完成日期： 2026-01-17
難度： Easy
標籤： Stack, Tree, Depth-First Search, Binary Tree
連結： LeetCode 94

## 題目描述
Given the root of a binary tree, return the inorder traversal of its nodes' values.

## 範例
**範例 1：**
Input: root = [1,null,2,3]
Output: [1,3,2]

**範例 2：**
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

**範例 3：**
Input: root = []
Output: []

**範例 4：**
Input: root = [1]
Output: [1]

## 限制條件
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Follow up
Recursive solution is trivial, could you do it iteratively?

## 解法：遞迴法（我的解法）
### 程式碼
```python
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
```

### 解題思路
1. **中序遍歷定義**：左子樹 → 根節點 → 右子樹
2. **遞迴終止條件**：當節點為空時返回空列表
3. **遞迴分解**：
   - 遍歷左子樹得到結果列表
   - 加入當前節點的值
   - 遍歷右子樹得到結果列表
4. **合併結果**：將三個部分用 `+` 運算符合併

## 我的思考過程
1. **問題分析**：需要按照特定順序遍歷二元樹的所有節點
2. **中序遍歷特性**：對於二元搜尋樹（BST），中序遍歷會得到排序後的結果
3. **選擇遞迴**：因為樹的結構天然適合遞迴處理
4. **實現細節**：
   - 使用 Python 列表的 `+` 運算符合併結果
   - 注意邊界條件：空樹返回空列表
   - 使用 `[root.val]` 將節點值轉為列表以便合併
5. **時間/空間考量**：遞迴解法簡潔，但可能會有遞迴深度的限制

## 關鍵點
- **中序遍歷順序**：左 → 根 → 右
- **遞迴終止條件**：節點為空時返回空列表
- **列表合併技巧**：使用 `+` 運算符合併多個列表
- **二元樹基本概念**：理解樹的節點結構（val, left, right）
- **邊界條件**：
  - 空樹（root 為 None）
  - 只有根節點的樹
  - 不平衡的樹

## 複雜度分析
- **時間複雜度**：O(n)
  - 每個節點只被訪問一次
  - n 是樹中節點的數量
- **空間複雜度**：O(n)
  - 遞迴調用棧深度：最壞情況 O(n)（當樹退化為鏈表時）
  - 平均情況 O(log n)（平衡樹時）
  - 結果列表：O(n)

## 測試範例
**測試 1**：root = [1,null,2,3]
→ 樹結構：1 為根，右子樹為 2，2 的左子樹為 3
→ 中序遍歷：3 → 2 → 1？不對，應該是：1 的左子樹（空）→ 1 → 2 的左子樹（3）→ 2 → 2 的右子樹（空）
→ 正確結果：[1,3,2]

**測試 2**：root = [1,2,3,4,5,null,8,null,null,6,7,9]
→ 複雜樹的中序遍歷
→ 結果：[4,2,6,5,7,1,3,9,8]

**測試 3**：root = []
→ 空樹，返回 []

**測試 4**：root = [1]
→ 只有根節點，返回 [1]

**測試 5**：root = [1,2,null,3,null,4]
→ 左傾斜的樹
→ 中序遍歷：[4,3,2,1]

## 學習心得
這題讓我學到：
1. **樹的遍歷基礎**：中序、前序、後序遍歷的差異
2. **遞迴在樹問題中的應用**：樹的結構天然適合遞迴處理
3. **二元樹資料結構**：理解 TreeNode 的定義和操作
4. **Python 列表操作**：使用 `+` 合併列表的技巧
5. **Follow up 挑戰**：題目鼓勵嘗試迭代解法，這對理解棧的操作很有幫助

## 相關題目
- 144. Binary Tree Preorder Traversal (Easy) - 前序遍歷
- 145. Binary Tree Postorder Traversal (Easy) - 後序遍歷
- 102. Binary Tree Level Order Traversal (Medium) - 層序遍歷
- 98. Validate Binary Search Tree (Medium) - 驗證二元搜尋樹（利用中序遍歷特性）

## 下一步計畫
- 嘗試迭代解法（使用棧）
- 練習其他樹的遍歷方式（前序、後序、層序）
- 學習更多樹相關的演算法
