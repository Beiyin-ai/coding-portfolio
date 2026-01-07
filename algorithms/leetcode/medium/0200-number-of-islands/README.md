# 200. Number of Islands

**完成日期：** 2026-01-07
**難度：** Medium
**標籤：** Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
**連結：** [LeetCode 200](https://leetcode.com/problems/number-of-islands/)

## 題目描述
給定一個 m x n 的二維二進位網格 `grid`，表示由 '1'（陸地）和 '0'（水域）組成的地圖。請返回島嶼的數量。

一個島嶼被水環繞，由相鄰的陸地水平或垂直連接形成。你可以假設網格的四個邊緣都被水環繞。

### 範例

**範例 1：**
```
輸入: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
輸出: 1
```

**範例 2：**
```
輸入: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
輸出: 3
```

### 限制條件
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` 為 '0' 或 '1'。

## 解法：深度優先搜索（我的解法）

### 程式碼
```python
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count
```

### 解題思路
1. **網格遍歷：**
   - 遍歷整個二維網格，對每個格子進行檢查
   - 當遇到 '1'（陸地）時，表示發現一個新的島嶼

2. **深度優先搜索 (DFS)：**
   - 發現陸地後，使用 DFS 遍歷所有相連的陸地
   - 將訪問過的陸地標記為 '0'（水域），避免重複計數
   - 遞迴檢查四個方向：上、下、左、右

3. **算法步驟：**
   - 初始化島嶼計數為 0
   - 雙層迴圈遍歷網格
   - 遇到 '1' 時，島嶼計數加 1，並執行 DFS
   - DFS 會將相連的所有 '1' 標記為 '0'
   - 返回島嶼總數

### 關鍵點
- **原地修改：** 直接修改輸入網格，將訪問過的陸地標記為水域
- **遞迴搜索：** 使用 DFS 探索相連的陸地區域
- **邊界檢查：** DFS 中檢查座標是否超出網格範圍
- **終止條件：** 遇到水域或超出邊界時停止遞迴

### 複雜度分析
- **時間複雜度：** O(m × n)
  - 每個格子最多被訪問一次
  - DFS 的遞迴深度最多為 m × n（全部為陸地的情況）
- **空間複雜度：** O(m × n)
  - 最壞情況下（全部為陸地），遞迴調用棧的深度為 m × n
  - 如果使用迭代或 BFS，空間複雜度可以降為 O(min(m, n))

### 測試範例
```python
# 測試 1: 範例 1
grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
# 輸出: 1

# 測試 2: 範例 2
grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
# 輸出: 3

# 測試 3: 空網格
grid3 = []
# 輸出: 0

# 測試 4: 全部水域
grid4 = [
    ["0","0","0"],
    ["0","0","0"],
    ["0","0","0"]
]
# 輸出: 0

# 測試 5: 全部陸地
grid5 = [
    ["1","1","1"],
    ["1","1","1"],
    ["1","1","1"]
]
# 輸出: 1
```

## 其他解法

### 解法2：廣度優先搜索 (BFS)
```python
from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"
            
            while queue:
                row, col = queue.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        
        return count
```

### 解法3：並查集 (Union Find)
```python
class UnionFind:
    def __init__(self, grid):
        rows, cols = len(grid), len(grid[0])
        self.parent = [i for i in range(rows * cols)]
        self.rank = [0] * (rows * cols)
        self.count = 0
        
        # 初始化：每個陸地都是一個獨立的集合
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self.count += 1
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路徑壓縮
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(grid)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # 檢查右邊和下邊的相鄰格子
                    if c + 1 < cols and grid[r][c+1] == "1":
                        uf.union(r * cols + c, r * cols + (c + 1))
                    if r + 1 < rows and grid[r+1][c] == "1":
                        uf.union(r * cols + c, (r + 1) * cols + c)
        
        return uf.count
```

## 解題思路比較

| 方法 | 時間複雜度 | 空間複雜度 | 特點 |
|------|-----------|-----------|------|
| 深度優先搜索 (DFS) | O(m × n) | O(m × n) | 遞迴實作，程式碼簡潔 |
| 廣度優先搜索 (BFS) | O(m × n) | O(min(m, n)) | 使用佇列，避免遞迴深度過大 |
| 並查集 (Union Find) | O(m × n × α(m×n)) | O(m × n) | 適合動態連接問題，α 是反阿克曼函數 |

## 學習心得
這題讓我學到：

1. **網格遍歷模式**：處理二維矩陣問題的基本技巧
2. **圖的遍歷算法**：DFS 和 BFS 在網格上的應用
3. **原地修改技巧**：通過修改輸入來節省空間
4. **並查集應用**：解決連接性問題的強大資料結構

這是典型的圖論問題，在網格上應用圖遍歷算法！

## 相關題目
- 695. Max Area of Island (Medium)
- 1254. Number of Closed Islands (Medium)
- 1905. Count Sub Islands (Medium)
- 130. Surrounded Regions (Medium)
- 463. Island Perimeter (Easy)

## 下一步計畫
1. 練習使用 BFS 實作同樣問題
2. 學習並查集的更多應用
3. 嘗試解決相關的島嶼問題變形
