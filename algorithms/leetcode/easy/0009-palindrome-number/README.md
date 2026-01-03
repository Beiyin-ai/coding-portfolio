# 9. Palindrome Number

**完成日期：** 2025-12-23  

## 學習歷程
這題學習了兩種判斷回文數的方法！

## 解法 1：字串反轉法（簡單直觀）

### 程式碼
```python
def isPalindrome_string(self, x: int) -> bool:
    if x < 0:
        return False
    
    s = str(x)
    return s == s[::-1]
```

### 解題思路
1. 負數直接返回 False（負號影響回文判斷）
2. 將整數轉為字串
3. 比較字串和它的反轉是否相同

### 複雜度分析
- **時間複雜度：O(n)**，n為數字位數
- **空間複雜度：O(n)**，需要儲存字串

### 優缺點
- 優點：簡單易懂，一行程式碼
- 缺點：需要額外空間

## 解法 2：數學反轉法（空間優化）

### 程式碼
```python
def isPalindrome_math(self, x: int) -> bool:
    if x < 0:
        return False
    
    original = x
    reversed_num = 0
    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    return original == reversed_num
```

### 解題思路
1. 負數直接返回 False
2. 保存原始數字
3. 用數學方法反轉數字：
   - 取得最後一位數字（x % 10）
   - 加到反轉數字中（reversed_num * 10 + digit）
   - 移除最後一位（x //= 10）
4. 比較原始數字和反轉後數字

### 複雜度分析
- **時間複雜度：O(n)**，n為數字位數
- **空間複雜度：O(1)**，只使用常數空間

### 優缺點
- 優點：空間效率高
- 缺點：需要處理數學運算

## 測試結果
所有測試案例都通過！✓

## 學習心得
1. **問題轉化**：將數字問題轉為字串問題可以簡化思考
2. **空間取捨**：字串法簡單但耗空間，數學法複雜但省空間
3. **邊界條件**：注意負數和0的處理
4. **多重解法**：同一個問題可以用不同角度解決
