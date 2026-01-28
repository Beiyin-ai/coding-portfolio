#!/usr/bin/env python3
"""
硬體連線測試
"""

import subprocess
import sys

def run_command(cmd):
    """執行指令並返回輸出"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return -1, "", str(e)

print("=" * 50)
print("硬體連線測試")
print("=" * 50)

# 測試 1: 檢查 USB 裝置
print("\n[測試 1] 檢查 USB 裝置...")
code, out, err = run_command("lsusb | grep -i 'CH341\\|1a86:7523'")
if code == 0:
    print("✅ 找到 CH341 USB 轉 TTL 裝置")
    print(f"   裝置: {out.strip()}")
else:
    print("❌ 未找到 CH341 裝置")
    print("   請檢查 USB 線連接")

# 測試 2: 檢查序列埠
print("\n[測試 2] 檢查序列埠...")
code, out, err = run_command("ls -la /dev/ttyUSB* 2>/dev/null || echo '未找到'")
if "ttyUSB" in out:
    print("✅ 找到序列埠裝置")
    for line in out.strip().split('\n'):
        if 'ttyUSB' in line:
            print(f"   {line}")
else:
    print("❌ 未找到 /dev/ttyUSB* 裝置")

# 測試 3: 檢查 Python 套件
print("\n[測試 3] 檢查 Python 套件...")
packages = ['opencv-python', 'mediapipe', 'pyserial']
for pkg in packages:
    # 處理套件名稱轉換
    import_name = pkg.replace('-', '_')
    if '[' in import_name:
        import_name = import_name.split('[')[0]
    
    code, out, err = run_command(f"python3 -c \"import {import_name}; print('OK')\" 2>&1")
    if "OK" in out or code == 0:
        print(f"✅ {pkg} 已安裝")
    else:
        print(f"❌ {pkg} 未安裝")

print("\n" + "=" * 50)
print("測試完成")
print("=" * 50)
print("\n建議下一步：")
print("1. 執行 ./setup.sh 安裝缺少的套件")
print("2. 執行 ./run.sh 啟動主程式")
print("3. 如有問題，參考 docs/TROUBLESHOOTING.md")
