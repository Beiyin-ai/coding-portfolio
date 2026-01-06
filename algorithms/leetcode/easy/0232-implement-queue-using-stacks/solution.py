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


# 測試用例
if __name__ == "__main__":
    # 測試示例
    myQueue = MyQueue()
    myQueue.push(1)   # queue: [1]
    myQueue.push(2)   # queue: [1, 2]
    print(myQueue.peek())   # 返回 1
    print(myQueue.pop())    # 返回 1, queue: [2]
    print(myQueue.empty())  # 返回 False
    print(myQueue.pop())    # 返回 2, queue: []
    print(myQueue.empty())  # 返回 True
