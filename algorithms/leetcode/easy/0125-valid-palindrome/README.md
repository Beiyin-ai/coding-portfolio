125. Valid Palindrome
完成日期： 2026-01-12
難度： Easy
標籤： Two Pointers, String
連結： LeetCode 125

## 題目描述
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## 範例
**範例 1：**
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

**範例 2：**
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

**範例 3：**
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

## 限制條件
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

## 解法：Python 字串操作（我的解法）
### 程式碼
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ 判斷是否為回文
        
        使用 Python 內建函式過濾非字母數字字元並轉小寫
        然後比較字串與其反轉是否相同
        這是我的解法，簡潔直觀
        """
        # 過濾非字母數字字元並轉為小寫
        palin = ''.join(ch.lower() for ch in s if ch.isalnum())
        # 比較字串與反轉字串
        return palin == palin[::-1]
```

### 解題思路
1. **字串預處理**：使用 `isalnum()` 過濾出字母數字字元，並用 `lower()` 轉為小寫
2. **反轉比較**：將處理後的字串與其反轉版本比較
3. **判斷結果**：相同則為回文，不同則不是

## 我的思考過程
1. **問題分析**：需要判斷處理過後的字串是否對稱
2. **Python 特性**：想到可以使用字串的 `isalnum()` 和 `lower()` 方法簡化處理
3. **回文判斷**：最簡單的方式是比較字串與其反轉
4. **效率考量**：雖然建立新字串需要額外空間，但程式碼簡潔易懂

## 關鍵點
- **字串處理**：`isalnum()` 判斷是否為字母數字，`lower()` 轉小寫
- **回文判斷技巧**：比較字串與其反轉（`s[::-1]`）是最直接的方法
- **邊界條件**：
  - 空字串：過濾後為空字串，空字串反轉仍是空字串，返回 true
  - 全是符號：過濾後為空字串，同樣返回 true
  - 單一字元：無論是否為字母數字，過濾後判斷

## 複雜度分析
- **時間複雜度**：O(n)
  - 需要遍歷字串一次進行過濾：O(n)
  - 建立新字串：O(n)
  - 比較字串與反轉：O(n)
  - 總時間複雜度：O(n)
- **空間複雜度**：O(n)
  - 需要額外空間儲存過濾後的字串

## 測試範例
**測試 1**："A man, a plan, a canal: Panama"
→ 過濾後："amanaplanacanalpanama"，返回 true

**測試 2**："race a car"
→ 過濾後："raceacar"，返回 false

**測試 3**：" "
→ 過濾後：""，返回 true

**測試 4**："0P"
→ 過濾後："0p"，反轉為 "p0"，返回 false

**測試 5**："a."
→ 過濾後："a"，返回 true

## 學習心得
這題讓我學到：
1. **Python 字串方法**：`isalnum()`、`lower()` 的實際應用
2. **回文問題的簡化解法**：直接比較字串與反轉字串
3. **字串處理技巧**：如何過濾特定字元並轉換大小寫
4. **邊界情況考慮**：空字串、全符號字串等特殊情況

## 相關題目
- 9. Palindrome Number (Easy) - 判斷數字是否為回文
- 234. Palindrome Linked List (Easy) - 判斷鏈表是否為回文
- 680. Valid Palindrome II (Easy) - 這題的進階版，允許刪除一個字元

## 下一步計畫
- 嘗試用雙指針解決同一問題（降低空間複雜度）
- 挑戰 680. Valid Palindrome II
- 練習更多字串處理相關的題目
