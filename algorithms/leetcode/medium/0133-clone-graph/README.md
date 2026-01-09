133. Clone Graph
完成日期： 2026-01-09
難度： Medium
標籤： Hash Table, Depth-First Search, Breadth-First Search, Graph
連結： LeetCode 133

## 題目描述
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

## 範例
**範例 1：**
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

**範例 2：**
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

**範例 3：**
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

## 限制條件
- 0 <= number of nodes <= 100
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

## 解法：深度優先搜索（我的解法）
### 程式碼
```python
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
```

### 解題思路
1. **建立映射表**：使用字典（hash map）儲存原始節點與複製節點的對應關係
2. **深度優先搜索**：從給定節點開始遍歷整個圖
3. **避免重複複製**：如果節點已經在映射表中，直接返回複製的節點
4. **遞迴複製**：先複製當前節點，然後遞迴複製所有鄰居節點

## 我的思考過程
1. **問題轉化**：這題是要深拷貝一個圖，需要複製所有節點和邊
2. **關鍵挑戰**：如何避免無限循環（因為圖可能有環）和重複複製節點
3. **解決方案**：使用 HashMap 記錄已複製的節點，這樣可以：
   - 避免重複創建相同節點
   - 避免無限遞迴
4. **選擇 DFS**：DFS 可以自然地處理圖的遍歷，程式碼較簡潔

## 關鍵點
- **HashMap 的使用**：這是解決圖複製問題的關鍵，用來建立原始節點和複製節點的映射
- **遞迴邊界條件**：當節點已經在 HashMap 中時直接返回，這防止了無限遞迴
- **空圖處理**：輸入可能為 None 或空圖，需要特別處理
- **鄰居連接**：複製節點時要確保正確連接鄰居關係

## 複雜度分析
- **時間複雜度**：O(V + E)
  - V：節點數量
  - E：邊的數量
  - 每個節點和邊只訪問一次
- **空間複雜度**：O(V)
  - HashMap 儲存所有節點的映射關係：O(V)
  - 遞迴調用棧深度：最壞情況 O(V)（當圖退化為鏈表時）

## 測試範例
**測試 1**：[[2,4],[1,3],[2,4],[1,3]]
→ 應該成功複製整個圖，結構相同但節點是新的

**測試 2**：[[]]
→ 只有一個節點且沒有鄰居

**測試 3**：[]
→ 空圖，返回 None

**測試 4**：[[2],[1]]
→ 兩個節點互相連接

## 學習心得
這題讓我學到：
1. **圖的基本操作**：如何遍歷和複製圖結構
2. **避免無限循環的技巧**：使用 HashMap 記錄已訪問節點是處理圖問題的常見技巧
3. **DFS 在圖中的應用**：遞迴 DFS 非常適合這類問題
4. **物件複製的細節**：深拷貝需要複製整個結構，而不只是參考
5. **邊界條件的重要性**：空圖、單節點圖等特殊情況需要仔細處理

## 相關題目
- 138. Copy List with Random Pointer (Medium) - 類似概念，複製帶有隨機指針的鍊錶
- 207. Course Schedule (Medium) - 圖的遍歷應用
- 797. All Paths From Source to Target (Medium) - 圖的遍歷

## 下一步計畫
- 嘗試用 BFS 解決同一問題
- 練習更多圖相關的題目
- 學習圖的各種演算法（Dijkstra, Bellman-Ford 等）
