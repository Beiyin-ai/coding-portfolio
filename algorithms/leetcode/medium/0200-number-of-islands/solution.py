class Solution:
    def numIslands(self, grid):
        """
        計算島嶼數量
        
        解法：深度優先搜索 (DFS)
        時間複雜度：O(m × n)，其中 m 和 n 是網格的尺寸
        空間複雜度：O(m × n)，遞迴調用棧的深度
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            """
            深度優先搜索，將相連的陸地標記為已訪問
            
            參數：
            r: 當前行索引
            c: 當前列索引
            """
            # 邊界檢查和終止條件
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            # 標記當前陸地為已訪問（改為水域）
            grid[r][c] = "0"
            
            # 遞迴搜索四個方向：下、上、右、左
            dfs(r + 1, c)  # 下
            dfs(r - 1, c)  # 上
            dfs(r, c + 1)  # 右
            dfs(r, c - 1)  # 左
        
        # 遍歷整個網格
        for r in range(rows):
            for c in range(cols):
                # 發現未訪問的陸地（島嶼起點）
                if grid[r][c] == "1":
                    count += 1  # 增加島嶼計數
                    dfs(r, c)   # 將相連的陸地全部標記
        
        return count
