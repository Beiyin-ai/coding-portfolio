344. Reverse String
完成日期： 2026-01-11
難度： Easy
標籤： Two Pointers, String
連結： LeetCode 344

## 題目描述
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

## 範例
**範例 1：**
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

**範例 2：**
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

## 限制條件
- 1 <= s.length <= 10^5
- s[i] is a printable ASCII character.

## 解法：雙指針法（我的解法）
### 程式碼
```python
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """ 反轉字串
        
        使用雙指針從兩端向中間交換元素
        這是我的解法，時間複雜度 O(n)，空間複雜度 O(1)
        """
        left = 0
        right = len(s) - 1
        
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

### 解題思路
1. **使用雙指針技巧**：
   - 左指針  從開頭開始
   - 右指針  從結尾開始
2. **交換元素**：每次迭代交換左右指針指向的元素
3. **向中間移動**：交換後左指針向右移動，右指針向左移動
4. **終止條件**：當右指針小於或等於左指針時停止

## 我的思考過程
1. **問題分析**：需要原地反轉字串，不能使用額外空間
2. **靈感來源**：想到可以直接交換頭尾元素，然後向中間移動
3. **設計演算法**：
   - 初始化兩個指針分別指向頭尾
   - 當左指針小於右指針時繼續循環
   - 每次循環交換兩個指針的元素
   - 移動指針向中間靠攏
4. **Python 特性**：利用 Python 的多重賦值簡化交換操作

## 關鍵點
- **雙指針技巧**：這是反轉字串/陣列最經典的方法
- **原地操作**：完全符合題目要求的 O(1) 額外空間
- **交換技巧**：Python 中可以直接使用 `a, b = b, a` 交換變數
- **邊界條件**：
  - 空字串：不需要處理
  - 單一字元：循環不會執行
- **終止條件**：使用 `while right > left` 確保不會多交換一次

## 複雜度分析
- **時間複雜度**：O(n)
  - 需要遍歷一半的陣列（n/2 次交換）
  - 每個元素只被訪問一次
- **空間複雜度**：O(1)
  - 只使用了常數額外空間（兩個指針變數）
  - 完全符合題目要求的原地修改

## 測試範例
**測試 1**：["h","e","l","l","o"]
→ 變為 ["o","l","l","e","h"]

**測試 2**：["H","a","n","n","a","h"]
→ 變為 ["h","a","n","n","a","H"]

**測試 3**：[]
→ 保持 []

**測試 4**：["a"]
→ 保持 ["a"]

**測試 5**：["a","b","c","d","e","f"]
→ 變為 ["f","e","d","c","b","a"]

## 學習心得
這題讓我學到：
1. **雙指針的經典應用**：反轉問題是雙指針最基礎的應用場景
2. **原地演算法設計**：如何在有限空間內完成操作
3. **Python 語法技巧**：利用多重賦值簡化交換操作
4. **演算法思維**：將問題分解為重複的簡單操作（交換）

## 相關題目
- 541. Reverse String II (Easy) - 反轉字串的變形
- 345. Reverse Vowels of a String (Easy) - 只反轉母音
- 151. Reverse Words in a String (Medium) - 反轉單詞
- 189. Rotate Array (Medium) - 旋轉陣列，也需要反轉操作

## 下一步計畫
- 嘗試解決 345. Reverse Vowels of a String
- 練習更多字串處理相關的題目
- 學習遞迴解法（雖然空間複雜度不符合要求）
