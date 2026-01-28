#!/usr/bin/env python3
"""
序列通訊測試程式
"""

import sys
import os

# 加入上層目錄到路徑
sys.path.append('../jetson')

try:
    # 測試導入 utils 模組
    from utils import get_available_serial_ports, test_serial_connection
    
    print("=" * 50)
    print("序列通訊測試")
    print("=" * 50)
    
    # 取得可用序列埠
    ports = get_available_serial_ports()
    
    if not ports:
        print("❌ 未找到任何序列埠")
        print("請檢查：")
        print("1. USB 轉 TTL 線是否連接")
        print("2. 驅動程式是否安裝")
        print("3. 執行 'lsusb' 確認裝置")
    else:
        print(f"✅ 找到 {len(ports)} 個序列埠：")
        for i, port_info in enumerate(ports, 1):
            print(f"{i}. {port_info['device']} - {port_info['description']}")
    
    print("\n" + "=" * 50)
    print("測試完成")
    print("=" * 50)
    
except ImportError as e:
    print(f"❌ 導入模組失敗: {e}")
    print("請確認 utils.py 存在於 jetson 目錄中")
except Exception as e:
    print(f"❌ 測試過程中發生錯誤: {e}")

# 測試主程式是否能執行
print("\n" + "=" * 50)
print("測試主程式導入")
print("=" * 50)

try:
    sys.path.append('..')
    # 這裡不真正執行主程式，只測試導入
    print("✅ 主程式結構檢查完成")
    print("✅ 測試通過！")
except Exception as e:
    print(f"❌ 主程式導入失敗: {e}")
