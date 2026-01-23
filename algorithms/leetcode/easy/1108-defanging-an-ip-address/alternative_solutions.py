"""
1108. Defanging an IP Address - 其他解法
"""

def solution_split_join(address: str) -> str:
    """使用 split 和 join"""
    return '[.]'.join(address.split('.'))

def solution_manual(address: str) -> str:
    """手動遍歷字串"""
    result = []
    for char in address:
        if char == '.':
            result.append('[.]')
        else:
            result.append(char)
    return ''.join(result)

def solution_list_comprehension(address: str) -> str:
    """使用列表推導式"""
    return ''.join(['[.]' if c == '.' else c for c in address])

# 測試所有解法
if __name__ == "__main__":
    test_address = "192.168.1.1"
    
    solutions = [
        ("replace()", lambda x: x.replace('.', '[.]')),
        ("split+join", solution_split_join),
        ("manual", solution_manual),
        ("list comprehension", solution_list_comprehension),
    ]
    
    print("不同解法的比較：")
    for name, func in solutions:
        result = func(test_address)
        print(f"{name:20} → {result}")
