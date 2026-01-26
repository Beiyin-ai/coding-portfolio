"""
168. Excel Sheet Column Title - 其他解法
"""

def convertToTitle_recursive(columnNumber: int) -> str:
    """遞迴解法"""
    if columnNumber == 0:
        return ""
    columnNumber -= 1
    return convertToTitle_recursive(columnNumber // 26) + chr(columnNumber % 26 + ord('A'))

def convertToTitle_while_no_list(columnNumber: int) -> str:
    """不使用列表的解法"""
    result = ""
    while columnNumber > 0:
        columnNumber -= 1
        result = chr(columnNumber % 26 + ord('A')) + result
        columnNumber //= 26
    return result

def convertToTitle_divmod(columnNumber: int) -> str:
    """使用 divmod 的解法"""
    result = []
    while columnNumber > 0:
        columnNumber, remainder = divmod(columnNumber - 1, 26)
        result.append(chr(remainder + ord('A')))
    return ''.join(reversed(result))

# 比較所有解法
if __name__ == "__main__":
    test_cases = [1, 26, 27, 28, 701, 702, 703]
    
    solutions = [
        ("原始解法", lambda n: Solution().convertToTitle(n)),
        ("遞迴解法", convertToTitle_recursive),
        ("無列表解法", convertToTitle_while_no_list),
        ("divmod解法", convertToTitle_divmod),
    ]
    
    print("不同解法的比較：")
    print("=" * 60)
    
    for name, func in solutions:
        print(f"\n{name}:")
        for num in test_cases:
            result = func(num)
            print(f"  {num:4d} → {result}")
