1528. Shuffle String
完成日期： 2026-01-25
難度： Easy
標籤： Array, String
連結： LeetCode 1528

## 題目描述
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

## 範例
**範例 1：**
```
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
```

**範例 2：**
```
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
```

**範例 3：**
```
Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"
```

## 限制條件
- s.length == indices.length == n
- 1 <= n <= 100
- s consists of only lowercase English letters.
- 0 <= indices[i] < n
- All values of indices are unique.

## 解法一：使用字典映射（我的第一次解法）
### 程式碼
```python
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """ 重新排列字串
        
        解法一：使用字典建立索引到字元的映射
        我的第一次解法
        """
        sMap = {}
        result = ""
        for i in range(len(s)):
            sMap[i] = s[i]          # 建立索引到字元的映射
        for j in indices:
            result += sMap[j]       # 按 indices 的順序取字元
        return result
```

### 解題思路
1. **建立映射**：先建立一個字典，將原始索引對應到字元
2. **遍歷 indices**：按照 indices 數組的順序，從字典中取出對應的字元
3. **構建結果**：將取出的字元依次加入結果字串

### 複雜度分析
- **時間複雜度**：O(n)
  - 第一次迴圈建立字典：O(n)
  - 第二次迴構建結果：O(n)
  - 總共 O(2n) = O(n)
- **空間複雜度**：O(n)
  - 字典儲存 n 個鍵值對：O(n)
  - 結果字串：O(n)

## 解法二：直接數組操作（我的第二種解法）
### 程式碼
```python
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """ 重新排列字串
        
        解法二：直接使用數組操作
        我的第二種解法，更高效
        """
        result = [''] * len(s)      # 建立一個固定長度的空陣列
        for i, char in enumerate(s):
            result[indices[i]] = char   # 把字元放到指定位置
        return ''.join(result)      # 合併成字串
```

### 解題思路
1. **建立空數組**：建立一個與原字串等長的空數組
2. **一次遍歷**：同時遍歷字元和 indices，將字元放到結果數組的指定位置
3. **合併結果**：使用 `join()` 將數組合併為字串

### 複雜度分析
- **時間複雜度**：O(n)
  - 單次迴圈遍歷：O(n)
  - `join()` 操作：O(n)
  - 總共 O(2n) = O(n)
- **空間複雜度**：O(n)
  - 結果數組：O(n)

## 我的思考過程
### 第一次解法（字典映射）
1. **初步理解**：題目要求按照 indices 的順序重排字元
2. **直覺思路**：先建立索引到字元的對應關係，再按照 indices 順序取字元
3. **實現細節**：
   - 使用字典儲存映射關係
   - 兩次迴圈：一次建立映射，一次構建結果

### 第二次解法（數組操作）
1. **優化思考**：第一次解法需要兩次迴圈，是否有更高效的方法？
2. **觀察發現**：indices[i] 告訴我們第 i 個字元應該放在結果的哪個位置
3. **改進實現**：
   - 建立固定大小的結果數組
   - 一次迴圈直接放置字元到正確位置
   - 使用 `enumerate()` 同時獲取索引和字元

## 兩種解法的比較
| 特性 | 解法一（字典映射） | 解法二（數組操作） |
|------|-------------------|------------------|
| **思路** | 建立映射再取用 | 直接放置到指定位置 |
| **迴圈次數** | 2 次 | 1 次 |
| **時間複雜度** | O(n) | O(n) |
| **空間複雜度** | O(n) | O(n) |
| **效率** | 較低（兩次遍歷） | 較高（一次遍歷） |
| **可讀性** | 直觀易懂 | 簡潔高效 |

## 關鍵點
1. **數組索引操作**：理解 indices 的意義 - indices[i] 表示原始位置 i 的字元應該放在結果的哪個位置
2. **Python 內建函數**：善用 `enumerate()` 同時獲取索引和值
3. **字串操作**：使用 `join()` 合併數組比字串拼接更高效
4. **空間預分配**：先建立固定大小的數組可以避免動態擴展的開銷

## 測試範例
### 測試 1：
- s = "codeleet", indices = [4,5,6,7,0,2,1,3]
- 解法二過程：
  - result = ['', '', '', '', '', '', '', '']
  - i=0, char='c', indices[0]=4 → result[4]='c'
  - i=1, char='o', indices[1]=5 → result[5]='o'
  - ... 依此類推
  - 最終 result = ['l','e','e','t','c','o','d','e']
  - join() → "leetcode"

### 測試 2：
- s = "abc", indices = [0,1,2]
- 每個字元都在原位，結果仍為 "abc"

### 測試 3：
- s = "aiohn", indices = [3,1,4,2,0]
- 結果應為 "nihao"

## 學習心得
這題讓我學到：
1. **多種解法比較**：同一問題可以有不同的解決思路，思考多種解法有助於提升程式設計能力
2. **效能優化**：從兩次迴圈優化到一次迴圈，體現了演算法優化的過程
3. **數組操作**：理解如何通過索引直接操作數組元素
4. **問題轉化**：將字串重排問題轉化為數組索引操作問題
5. **Python 工具**：熟練使用 `enumerate()` 和 `join()` 等內建函數

## 相關題目
- 1470. Shuffle the Array (Easy) - 類似的重排問題
- 344. Reverse String (Easy) - 字串操作
- 189. Rotate Array (Medium) - 數組重排
- 48. Rotate Image (Medium) - 二維數組操作

## 下一步計畫
- 嘗試更多數組和字串操作的題目
- 練習一題多解的思考方式
- 學習時間和空間複雜度的分析
