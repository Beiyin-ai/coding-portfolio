# 232. 用堆疊實現佇列

## 問題描述
請僅使用兩個堆疊實現一個先入先出（FIFO）的佇列。佇列應當支援一般佇列支援的所有操作（`push`、`peek`、`pop`、`empty`）。

實現 `MyQueue` 類別：
- `void push(int x)` 將元素 `x` 推到佇列的末尾
- `int pop()` 從佇列的開頭移除並返回元素
- `int peek()` 返回佇列開頭的元素
- `boolean empty()` 如果佇列為空，返回 `true`；否則返回 `false`

**注意：**
- 你只能使用堆疊的標準操作：`push`、`pop`、`peek`、`size` 和 `empty`
- 取決於你的語言，堆疊可能不被原生支援。你可以使用 list 或 deque 來模擬堆疊，只要是標準的堆疊操作即可

## 解題思路

### 方法：雙堆疊法
使用兩個堆疊來模擬佇列：
1. **輸入堆疊（inStack）**：專門用於 `push` 操作
2. **輸出堆疊（outStack）**：專門用於 `pop` 和 `peek` 操作

**關鍵操作：**
- `push(x)`：直接將元素壓入 `inStack`
- `pop()`：
  - 如果 `outStack` 為空，將 `inStack` 的所有元素轉移到 `outStack`
  - 從 `outStack` 彈出並返回頂部元素
- `peek()`：
  - 如果 `outStack` 為空，將 `inStack` 的所有元素轉移到 `outStack`
  - 返回 `outStack` 的頂部元素（不彈出）
- `empty()`：當兩個堆疊都為空時，佇列為空

### 時間複雜度分析（均攤分析）
- **push(x)**：O(1)
- **pop()**：均攤 O(1)（最壞情況 O(n)，但每個元素只會被移動一次）
- **peek()**：均攤 O(1)
- **empty()**：O(1)

### 代碼實現
```python
class MyQueue:
    def __init__(self):
        """初始化兩個堆疊：輸入堆疊和輸出堆疊"""
        self.inStack = []   # 用於 push 操作
        self.outStack = []  # 用於 pop 和 peek 操作

    def push(self, x: int) -> None:
        """將元素推入佇列尾部"""
        self.inStack.append(x)

    def pop(self) -> int:
        """從佇列頭部移除並返回元素"""
        # 如果輸出堆疊為空，則將輸入堆疊的所有元素轉移到輸出堆疊
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self) -> int:
        """返回佇列頭部的元素但不移除"""
        # 如果輸出堆疊為空，則將輸入堆疊的所有元素轉移到輸出堆疊
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self) -> bool:
        """檢查佇列是否為空"""
        return not self.inStack and not self.outStack
```

### 示例
```python
myQueue = MyQueue()
myQueue.push(1)   # 佇列: [1]
myQueue.push(2)   # 佇列: [1, 2]
print(myQueue.peek())   # 返回 1
print(myQueue.pop())    # 返回 1, 佇列: [2]
print(myQueue.empty())  # 返回 False
print(myQueue.pop())    # 返回 2, 佇列: []
print(myQueue.empty())  # 返回 True
```

### 算法原理圖解
```
操作順序：
1. push(1) → inStack: [1], outStack: []
2. push(2) → inStack: [1, 2], outStack: []
3. peek() → 移動元素到outStack → inStack: [], outStack: [2, 1] → 返回1
4. pop() → outStack彈出1 → inStack: [], outStack: [2] → 返回1
5. push(3) → inStack: [3], outStack: [2]
6. pop() → outStack彈出2 → inStack: [3], outStack: [] → 返回2
```

### 與第155題（Min Stack）的對比
| 特性 | 第155題 Min Stack | 第232題 Queue using Stacks |
|------|------------------|--------------------------|
| 目標 | 實現有最小值的堆疊 | 用堆疊實現佇列 |
| 數據結構 | 兩個堆疊（一個存數據，一個存最小值） | 兩個堆疊（一個用於push，一個用於pop/peek） |
| 核心思想 | 輔助堆疊追蹤最小值 | 利用堆疊反轉順序實現FIFO |
| 時間複雜度 | 所有操作O(1) | push: O(1), pop/peek: 均攤O(1) |

### 應用場景
1. **面試常見題**：考察對數據結構的理解和轉換能力
2. **系統設計**：在資源受限環境中，用現有結構實現所需功能
3. **算法理解**：幫助理解堆疊和佇列的本質差異
4. **均攤分析練習**：理解均攤時間複雜度的概念
