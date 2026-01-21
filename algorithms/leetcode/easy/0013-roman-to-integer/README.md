13. Roman to Integer
完成日期： 2026-01-21
難度： Easy
標籤： Hash Table, Math, String
連結： LeetCode 13

## 題目描述
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## 範例
**範例 1：**
Input: s = "III"
Output: 3
Explanation: III = 3.

**範例 2：**
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

**範例 3：**
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

## 限制條件
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## 解法：從左到右掃描（我的解法）
### 程式碼
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        """ 羅馬數字轉整數
        
        使用字典儲存羅馬數字對應值，從左到右掃描
        如果當前數字比下一個小，則減去當前值，否則加上當前值
        這是我的解法，時間複雜度 O(n)，空間複雜度 O(1)
        """
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        for i in range(len(s)):
            # 如果下一個比當前大 → 減法規則
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
```

### 解題思路
1. **建立映射表**：使用字典儲存羅馬數字到整數的對應關係
2. **從左到右掃描**：遍歷羅馬數字的每個字符
3. **處理減法規則**：如果當前字符對應的值小於下一個字符的值，則減去當前值
4. **處理加法規則**：否則，加上當前值
5. **累加結果**：最後的總和即為轉換後的整數

## 我的思考過程
1. **問題分析**：需要將羅馬數字轉換為整數，需處理特殊的減法規則
2. **觀察規律**：羅馬數字通常從大到小排列，但有六種特殊情況需要減法：
   - IV (4), IX (9)
   - XL (40), XC (90)
   - CD (400), CM (900)
3. **設計算法**：從左到右掃描，比較當前字符和下一個字符的值
4. **實現細節**：
   - 使用字典快速查找字符對應的值
   - 注意邊界條件：最後一個字符沒有下一個字符
   - 使用索引範圍檢查避免越界
5. **驗證算法**：用幾個例子測試算法的正確性

## 關鍵點
- **字典映射**：使用字典儲存羅馬數字到整數的映射關係
- **減法規則**：當前字符值 < 下一個字符值時，執行減法
- **邊界處理**：最後一個字符不需要檢查下一個字符
- **羅馬數字規則**：理解六種特殊的減法組合
- **時間複雜度**：O(n)，只需要一次遍歷
- **空間複雜度**：O(1)，字典大小固定（7個元素）

## 複雜度分析
- **時間複雜度**：O(n)
  - n 是羅馬數字的長度
  - 只需要一次遍歷
  - 字典查找操作是 O(1)
- **空間複雜度**：O(1)
  - 字典大小固定為 7
  - 只使用幾個變數儲存結果和中間值

## 測試範例
**測試 1**：s = "III"
→ 遍歷過程：
  I: 1 (無下一個或下一個不大) → +1 = 1
  I: 1 (無下一個或下一個不大) → +1 = 2
  I: 1 (無下一個或下一個不大) → +1 = 3
→ 結果：3

**測試 2**：s = "LVIII"
→ 遍歷過程：
  L: 50 (下一個 V=5 不大) → +50 = 50
  V: 5 (下一個 I=1 不大) → +5 = 55
  I: 1 (下一個 I=1 不大) → +1 = 56
  I: 1 (下一個 I=1 不大) → +1 = 57
  I: 1 (無下一個) → +1 = 58
→ 結果：58

**測試 3**：s = "MCMXCIV"
→ 遍歷過程：
  M: 1000 (下一個 C=100 不大) → +1000 = 1000
  C: 100 (下一個 M=1000 更大) → -100 = 900
  M: 1000 (下一個 X=10 不大) → +1000 = 1900
  X: 10 (下一個 C=100 更大) → -10 = 1890
  C: 100 (下一個 I=1 不大) → +100 = 1990
  I: 1 (下一個 V=5 更大) → -1 = 1989
  V: 5 (無下一個) → +5 = 1994
→ 結果：1994

**測試 4**：s = "IV"
→ 遍歷過程：
  I: 1 (下一個 V=5 更大) → -1 = -1
  V: 5 (無下一個) → +5 = 4
→ 結果：4

**測試 5**：s = "IX"
→ 結果：9

## 學習心得
這題讓我學到：
1. **羅馬數字規則**：理解羅馬數字的表示方法和特殊的減法規則
2. **字典的應用**：如何使用字典快速映射字符到數值
3. **從右到左思考**：雖然程式從左到右掃描，但理解從右到左的累加邏輯
4. **邊界條件處理**：如何安全地檢查下一個字符而不越界
5. **數學轉換技巧**：將複雜規則轉化為簡單的比較和加減操作

## 相關題目
- 12. Integer to Roman (Medium) - 整數轉羅馬數字（反向操作）
- 273. Integer to English Words (Hard) - 整數轉英文單詞
- 65. Valid Number (Hard) - 驗證數字字串
- 8. String to Integer (atoi) (Medium) - 字串轉整數

## 下一步計畫
- 嘗試解決 12. Integer to Roman（反向問題）
- 練習更多字串處理相關的題目
- 學習正則表達式處理數字格式
