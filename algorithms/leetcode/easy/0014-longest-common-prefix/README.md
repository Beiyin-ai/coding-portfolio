14. Longest Common Prefix
完成日期： 2026-01-13
難度： Easy
標籤： String, Trie
連結： LeetCode 14

## 題目描述
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## 範例
**範例 1：**
Input: strs = ["flower","flow","flight"]
Output: "fl"

**範例 2：**
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

## 限制條件
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters if it is non-empty.

## 解法：逐字比較法（我的解法）
### 程式碼
```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ 尋找最長共同前綴
        
        使用第一個字串作為初始前綴，逐步與其他字串比較並縮短
        這是我的解法，直觀且效率良好
        """
        if not strs:
            return ""
        
        # 使用第一個字串作為初始前綴
        prefix = strs[0]
        
        for s in strs[1:]:
            # 逐步縮短前綴直到符合當前字串
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix
```

### 解題思路
1. **初始化前綴**：以第一個字串作為初始最長共同前綴
2. **逐個比較**：與陣列中的每個字串進行比較
3. **縮短前綴**：如果當前字串不以該前綴開頭，則將前綴縮短一個字元
4. **終止條件**：前綴為空字串時返回，或所有字串比較完畢

## 我的思考過程
1. **問題分析**：需要找多個字串的共同開頭部分
2. **靈感來源**：想到可以用第一個字串作為基準，逐步與其他字串比對
3. **選擇演算法**：使用 `startswith()` 方法判斷，不匹配時縮短前綴
4. **邊界條件**：
   - 空陣列：直接返回空字串
   - 空字串在陣列中：前綴會縮短為空字串
   - 只有一個字串：直接返回該字串

## 關鍵點
- **`startswith()` 方法**：判斷字串是否以指定前綴開頭
- **逐步縮短策略**：從完整字串開始，逐步縮短直到找到共同前綴
- **時間優化**：當發現前綴為空時立即返回，避免不必要的比較
- **邊界處理**：
  - 輸入為空陣列
  - 陣列中有空字串
  - 陣列只有一個元素

## 複雜度分析
- **時間複雜度**：O(S)，其中 S 是所有字串的總字元數
  - 最壞情況：每個字串都需要比較到最後一個字元
  - 最佳情況：第一個字串就是最短的，或很快發現無共同前綴
- **空間複雜度**：O(1)
  - 只使用了常數額外空間（幾個變數儲存前綴）

## 測試範例
**測試 1**：["flower","flow","flight"]
→ 前綴從 "flower" 開始
→ 與 "flow" 比較："flower" 縮短為 "flowe" → "flow"，符合
→ 與 "flight" 比較："flow" 縮短為 "flo" → "fl"，符合
→ 返回 "fl"

**測試 2**：["dog","racecar","car"]
→ 前綴從 "dog" 開始
→ 與 "racecar" 比較："dog" 縮短為 "do" → "d" → ""，返回 ""

**測試 3**：["interspecies","interstellar","interstate"]
→ 返回 "inters"

**測試 4**：["","flower","flow"]
→ 前綴從 "" 開始，立即返回 ""

**測試 5**：["single"]
→ 直接返回 "single"

## 學習心得
這題讓我學到：
1. **字串前綴處理**：如何使用 `startswith()` 方法進行前綴判斷
2. **逐步縮減策略**：從完整解開始，逐步縮減到符合條件的解
3. **多字串比較技巧**：以第一個元素為基準，逐步與其他元素比對
4. **邊界條件重要性**：空陣列、空字串等特殊情況需要仔細處理

## 相關題目
- 208. Implement Trie (Prefix Tree) (Medium) - 前綴樹的實作
- 720. Longest Word in Dictionary (Easy) - 字典中最長單詞
- 821. Shortest Distance to a Character (Easy) - 字元的最短距離

## 下一步計畫
- 嘗試其他解法（如垂直掃描、分治法）
- 學習 Trie 資料結構的實作與應用
- 練習更多字串處理相關的題目
