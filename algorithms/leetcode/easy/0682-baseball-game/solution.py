from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """ 棒球遊戲計分
        
        使用數組模擬遊戲記錄的變化
        根據不同的操作進行相應的處理
        這是我的解法
        """
        record = []

        for op in operations:
            if op == "C":
                # 移除最後一個分數
                record.pop()
            elif op == "D":
                # 將最後一個分數乘以2後加入
                record.append(record[-1] * 2)
            elif op == "+":
                # 將最後兩個分數相加後加入
                record.append(record[-1] + record[-2])
            else:
                # 將字串轉為整數後加入
                record.append(int(op))
        
        return sum(record)


# 測試程式碼
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1", "C"], 0),
        (["5", "2", "+", "D", "C"], 14),
        (["5"], 5),
        (["5", "D", "D", "D"], 5 + 10 + 20 + 40),
    ]
    
    print("Baseball Game 測試結果：")
    print("=" * 50)
    
    all_passed = True
    for i, (ops, expected) in enumerate(test_cases, 1):
        result = solution.calPoints(ops)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        
        print(f"測試 {i}: {ops}")
        print(f"    結果: {result} {status} (預期: {expected})")
        print()
    
    print("=" * 50)
    if all_passed:
        print("✅ 所有測試通過！")
    else:
        print("❌ 有測試失敗！")
    
    # 顯示操作過程的詳細範例
    print("\n詳細操作過程（範例1）：")
    ops = ["5", "2", "C", "D", "+"]
    record = []
    print(f"操作: {ops}")
    for i, op in enumerate(ops):
        if op == "C":
            record.pop()
        elif op == "D":
            record.append(record[-1] * 2)
        elif op == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(op))
        print(f"  {op}: {record}")
    print(f"總和: {sum(record)}")
