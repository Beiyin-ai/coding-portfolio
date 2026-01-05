# 155. 最小堆疊

## 問題描述
設計一個支援 `push`、`pop`、`top` 操作，並能在常數時間內檢索到最小元素的堆疊。

實作 `MinStack` 類別：
- `MinStack()` 初始化堆疊物件
- `void push(int val)` 將元素 `val` 壓入堆疊
- `void pop()` 刪除堆疊頂部的元素
- `int top()` 獲取堆疊頂部的元素
- `int getMin()` 獲取堆疊中的最小元素

要求每個操作的時間複雜度都為 O(1)。

## 解題思路

### 方法：雙堆疊法
使用兩個堆疊來實現：
1. `stack`：正常的堆疊，用於存儲所有元素
2. `minStack`：最小堆疊，用於存儲當前的最小值

**關鍵點：**
- 當壓入新元素時，如果 `minStack` 為空或新值 ≤ `minStack` 的頂部值，則同時壓入 `minStack`
- 當彈出元素時，如果彈出的值等於 `minStack` 的頂部值，則同時從 `minStack` 彈出
- 這樣可以保證 `minStack` 的頂部始終是當前堆疊中的最小值

### 代碼實現
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        """將元素壓入堆疊"""
        self.stack.append(val)
        # 如果minStack為空或新值小於等於當前最小值，則更新minStack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        """彈出堆疊頂部元素"""
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        """獲取堆疊頂部元素"""
        return self.stack[-1]

    def getMin(self) -> int:
        """獲取堆疊中的最小元素"""
        return self.minStack[-1]
```

### 複雜度分析
- **時間複雜度:** O(1) 每個操作（push、pop、top、getMin）都是常數時間
- **空間複雜度:** O(n) 最壞情況下需要額外的 n 空間存儲最小堆疊

### 示例
```python
# 輸入
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

# 輸出
print(minStack.getMin())  # -3
minStack.pop()
print(minStack.top())     # 0
print(minStack.getMin())  # -2
```

### 邊界情況
1. **空堆疊處理：** 題目保證 `pop`、`top`、`getMin` 操作只在非空堆疊上呼叫
2. **重複最小值：** 使用 `<=` 而不是 `<` 來處理重複的最小值
3. **極端值：** 值範圍在 -2³¹ 到 2³¹-1 之間

### 其他方法
1. **單堆疊法：** 在堆疊中存儲元組 (value, current_min)，這樣只需一個堆疊但每個元素占用更多空間
2. **差值法：** 存儲與當前最小值的差值，可以進一步節省空間，但實現較複雜

### 應用場景
- 需要快速獲取當前數據流中的最小值
- 瀏覽器前進後退功能中的歷史記錄
- 編輯器的撤銷/重做功能
