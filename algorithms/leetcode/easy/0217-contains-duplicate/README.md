# 217. Contains Duplicate

**完成日期：** 2025-12-28  

## 學習歷程
這題記錄了我從基礎解法到優化解法的學習過程！

## 解法 1：暴力法（我的第一個想法）

### 程式碼
```python
def containsDuplicate_bruteforce(self, nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

### 解題思路
- 使用雙重迴圈比較所有組合
- 找到相同數字就返回 True
- 全部檢查完都沒找到就返回 False

### 複雜度分析
- **時間複雜度：O(n²)**
- **空間複雜度：O(1)**

## 解法 2：使用 Set（學習後改進）

### 程式碼
```python
def containsDuplicate_set(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```

### 解題思路
- 利用 set 自動去重複
- 比較原始長度和去重後長度
- 長度不同表示有重複

### 複雜度分析
- **時間複雜度：O(n)**
- **空間複雜度：O(n)**

## 學習心得
從暴力法 O(n²) 到 set 法 O(n)，學到了用空間換取時間的優化思路。

## 測試結果
所有測試案例都通過！✓
