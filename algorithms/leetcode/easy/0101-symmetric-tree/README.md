101. Symmetric Tree
完成日期： 2026-01-18
難度： Easy
標籤： Tree, Depth-First Search, Breadth-First Search, Binary Tree
連結： LeetCode 101

## 題目描述
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## 範例
**範例 1：**
Input: root = [1,2,2,3,4,4,3]
Output: true

**範例 2：**
Input: root = [1,2,2,null,3,null,3]
Output: false

## 限制條件
- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100

## 解法：遞迴檢查對稱性（我的解法）
### 程式碼
```python
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
```

### 解題思路
1. **定義鏡像關係**：兩棵樹互為鏡像當且僅當：
   - 它們的根節點值相等
   - 第一棵樹的左子樹與第二棵樹的右子樹互為鏡像
   - 第一棵樹的右子樹與第二棵樹的左子樹互為鏡像
2. **遞迴檢查**：從根節點開始，比較左右子樹是否互為鏡像
3. **邊界條件**：
   - 空樹：定義為對稱
   - 只有根節點：對稱
   - 節點值不相等：立即返回 false

## 我的思考過程
1. **問題分析**：需要檢查樹是否沿中心軸對稱
2. **關鍵觀察**：對稱樹的左右子樹互為鏡像關係
3. **設計遞迴函數**：
   - 比較兩個節點的值是否相等
   - 遞迴比較：node1.left 與 node2.right
   - 遞迴比較：node1.right 與 node2.left
4. **實現細節**：
   - 使用內部函數 `isMirror` 簡化邏輯
   - 處理空節點的邊界情況
   - 使用邏輯運算符 `and` 連接多個條件
5. **時間/空間考量**：遞迴解法直觀，但也可以考慮迭代解法

## 關鍵點
- **鏡像定義**：理解樹的鏡像關係是解題核心
- **遞迴結構**：樹的對稱性檢查天然適合遞迴
- **邊界條件處理**：空節點、單節點、不對稱節點
- **對稱檢查模式**：比較左-右和右-左的交叉比較
- **提前返回**：一旦發現不對稱立即返回，避免不必要的計算

## 複雜度分析
- **時間複雜度**：O(n)
  - 每個節點只被訪問一次
  - n 是樹中節點的數量
- **空間複雜度**：O(n)
  - 遞迴調用棧深度：最壞情況 O(n)（當樹退化為鏈表且對稱時）
  - 平均情況 O(log n)（平衡樹時）

## 測試範例
**測試 1**：root = [1,2,2,3,4,4,3]
→ 樹結構：
       1
     /   \
    2     2
   / \   / \
  3   4 4   3
→ 檢查過程：
  isMirror(2, 2) → True
  isMirror(3, 3) → True
  isMirror(4, 4) → True
→ 結果：True

**測試 2**：root = [1,2,2,null,3,null,3]
→ 樹結構：
       1
     /   \
    2     2
     \     \
      3     3
→ 檢查過程：
  isMirror(2, 2) → True
  isMirror(null, null) → True
  isMirror(3, 3) → True
  等等...不對，左子樹的右子樹 vs 右子樹的左子樹：3 vs null → False
→ 結果：False

**測試 3**：root = []
→ 空樹，返回 True

**測試 4**：root = [1]
→ 只有根節點，返回 True

**測試 5**：root = [1,2,3]
→ 不對稱，返回 False

## 學習心得
這題讓我學到：
1. **樹的對稱性概念**：如何定義和檢查樹的鏡像關係
2. **遞迴的進階應用**：處理兩個樹之間的比較關係
3. **交叉比較模式**：左-右和右-左的對稱比較技巧
4. **邊界條件的重要性**：空節點、單節點等特殊情況
5. **樹問題的思考框架**：從定義出發，設計遞迴條件

## 相關題目
- 100. Same Tree (Easy) - 檢查兩棵樹是否相同
- 104. Maximum Depth of Binary Tree (Easy) - 樹的最大深度
- 110. Balanced Binary Tree (Easy) - 平衡二元樹
- 226. Invert Binary Tree (Easy) - 翻轉二元樹

## 下一步計畫
- 嘗試迭代解法（使用佇列或堆疊）
- 解決 100. Same Tree 練習樹的比較
- 學習更多樹的變形問題
