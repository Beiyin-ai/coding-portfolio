# 序列埠設定詳細指南

## 📡 硬體偵測記錄
根據你的 `dmesg` 輸出，系統偵測到以下裝置：



**解讀：**
- 裝置型號：CH341 USB 轉 TTL 序列線
- 裝置路徑：`/dev/ttyUSB0`
- 驅動程式：ch341-uart
- VID:PID：1a86:7523 (CH341 標準識別碼)

## 🔍 檢查序列埠狀態

### 指令 1：查看所有序列埠


### 指令 2：查看 USB 裝置詳細資訊


### 指令 3：即時監控裝置連接狀態


## 🔧 權限設定方法

### 方法 A：加入使用者群組 (推薦)
sudo usermod -a -G tty codespace      # 終端機裝置權限

# 重新登入使變更生效
logout
# 或使用以下指令立即生效：
newgrp dialout


### 方法 B：手動修改權限 (暫時)


### 方法 C：建立 udev 規則 (永久自動)


## 🧪 測試序列通訊

### 測試 1：基本連線測試
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    print('✅ 序列埠開啟成功')
    
    # 等待 ESP32 初始化
    time.sleep(2)
    
    # 測試傳送資料
    ser.write(b'1\n')
    print('📤 傳送: 1 (白色燈光)')
    
    # 關閉序列埠
    ser.close()
    print('🔒 序列埠已關閉')
    
except serial.SerialException as e:
    print(f'❌ 錯誤: {e}')
    print('請檢查：')
    print('1. USB 線是否連接')
    print('2. 序列埠權限設定')
    print('3. 裝置是否被其他程式占用')


### 測試 2：互動式測試


### 測試 3：使用 minicom


## 🔄 程式自動偵測機制
主程式 `main.py` 包含自動偵測序列埠的功能：



## 📝 常見錯誤與解決方案

### 錯誤 1：serial.serialutil.SerialException: [Errno 13] Permission denied
**原因：** 使用者沒有序列埠的讀寫權限
**解決：** 執行權限設定 (方法 A、B 或 C)

### 錯誤 2：serial.serialutil.SerialException: could not open port
**原因：** 裝置不存在或被占用
**解決：**
1. 檢查 USB 線連接
2. 執行 `dmesg | grep tty` 確認裝置路徑
3. 檢查是否有其他程式占用：
   `sudo lsof /dev/ttyUSB0`

### 錯誤 3：裝置突然消失
**原因：** USB 接觸不良或電源不穩
**解決：**
1. 更換 USB 線或連接埠
2. 使用有外接電源的 USB Hub
3. 檢查 ESP32 電源供應

### 錯誤 4：資料傳送但 ESP32 無反應
**原因：** 波特率不一致或接線錯誤
**解決：**
1. 確認兩端波特率都是 9600
2. 檢查 TX-RX 是否交叉連接
3. 確認接地 (GND) 連接

## 🎯 最佳實務建議
1. **固定裝置路徑：** 使用 udev 規則為特定裝置建立固定別名
2. **電源管理：** 為 ESP32 和 LED 提供獨立穩定電源
3. **錯誤處理：** 在程式中加入序列通訊錯誤恢復機制
4. **日誌記錄：** 記錄序列通訊狀態，方便除錯
5. **熱插拔支援：** 監控裝置狀態，支援動態插拔

---
**相關文件：**
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - 完整設定指南
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - 故障排除
