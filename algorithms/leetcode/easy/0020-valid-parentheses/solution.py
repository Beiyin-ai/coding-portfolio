class Solution:
    def isValid(self, s: str) -> bool:
        """
        檢查括號是否有效匹配
        
        使用 stack 資料結構：
        1. 遇到開括號時推入 stack
        2. 遇到閉括號時檢查 stack 頂部是否匹配
        3. 最終檢查 stack 是否為空
        
        時間複雜度: O(n)
        空間複雜度: O(n)
        """
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        
        for ch in s:
            if ch in pairs.values():  # 開括號
                stack.append(ch)
            elif ch in pairs:         # 閉括號
                if not stack:         # stack 為空，沒有對應的開括號
                    return False
                if stack.pop() != pairs[ch]:  # 括號不匹配
                    return False
        
        # 所有括號都匹配成功時，stack 應該為空
        return not stack
