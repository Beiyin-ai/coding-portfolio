"""
682. Baseball Game - 其他解法
"""

from typing import List

def calPoints_using_stack(operations: List[str]) -> int:
    """更明確的棧實現"""
    stack = []
    
    for op in operations:
        if op == "C":
            if stack:
                stack.pop()
        elif op == "D":
            if stack:
                stack.append(stack[-1] * 2)
        elif op == "+":
            if len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    
    return sum(stack)

def calPoints_with_validation(operations: List[str]) -> int:
    """帶有驗證的解法（更安全）"""
    record = []
    
    for op in operations:
        if op == "C":
            if record:  # 驗證是否有元素可移除
                record.pop()
        elif op == "D":
            if record:  # 驗證是否有元素可參考
                record.append(record[-1] * 2)
        elif op == "+":
            if len(record) >= 2:  # 驗證是否有足夠元素
                record.append(record[-1] + record[-2])
        else:
            # 驗證是否為有效數字
            try:
                record.append(int(op))
            except ValueError:
                # 如果不是有效數字，可以選擇忽略或處理錯誤
                pass
    
    return sum(record)

def calPoints_one_pass_sum(operations: List[str]) -> int:
    """一次遍歷同時計算總和（節省空間）"""
    stack = []
    total = 0
    
    for op in operations:
        if op == "C":
            if stack:
                total -= stack.pop()
        elif op == "D":
            if stack:
                new_score = stack[-1] * 2
                stack.append(new_score)
                total += new_score
        elif op == "+":
            if len(stack) >= 2:
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
                total += new_score
        else:
            score = int(op)
            stack.append(score)
            total += score
    
    return total

# 比較所有解法
if __name__ == "__main__":
    test_cases = [
        ["5", "2", "C", "D", "+"],
        ["5", "-2", "4", "C", "D", "9", "+", "+"],
        ["1", "C"],
    ]
    
    solutions = [
        ("原始解法", Solution().calPoints),
        ("棧實現", calPoints_using_stack),
        ("帶驗證", calPoints_with_validation),
        ("一次計算", calPoints_one_pass_sum),
    ]
    
    print("不同解法的比較：")
    print("=" * 60)
    
    for ops in test_cases:
        print(f"\n測試案例: {ops}")
        for name, func in solutions:
            result = func(ops)
            print(f"  {name:15}: {result}")
