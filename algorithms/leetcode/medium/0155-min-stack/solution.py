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


# 測試用例
if __name__ == "__main__":
    # 測試示例
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # 返回 -3
    minStack.pop()
    print(minStack.top())     # 返回 0
    print(minStack.getMin())  # 返回 -2
