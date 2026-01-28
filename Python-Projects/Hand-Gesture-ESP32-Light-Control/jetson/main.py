#!/usr/bin/env python3
"""
Hand Gesture Recognition for ESP32 Light Control
Main program running on Jetson Nano
"""

import cv2
import mediapipe as mp
import serial
import time
import sys
import os

# --- 設定序列埠 ---
# 根據你的 dmesg 輸出，USB 序列線連接後是 /dev/ttyUSB0
# Jetson Nano 內建 UART 是 /dev/ttyTHS1
# 自動偵測可用序列埠
def find_serial_port():
    """自動尋找可用的序列埠"""
    possible_ports = [
        '/dev/ttyUSB0',    # USB 轉 TTL (CH341)
        '/dev/ttyTHS1',    # Jetson Nano 內建 UART
        '/dev/ttyACM0',    # USB CDC
        '/dev/ttyAMA0',    # Raspberry Pi UART
        'COM3',            # Windows
        'COM4',            # Windows
    ]
    
    for port in possible_ports:
        if os.path.exists(port):
            print(f"發現序列埠: {port}")
            return port
    
    print("警告: 未找到序列埠，使用測試模式")
    return None

SERIAL_PORT = find_serial_port()
BAUD_RATE = 9600

# 初始化序列通訊
ser = None
if SERIAL_PORT:
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # 等待 ESP32 啟動
        print(f"✓ 成功開啟序列埠: {SERIAL_PORT} @ {BAUD_RATE} baud")
    except Exception as e:
        print(f"✗ 序列埠開啟失敗: {e}")
        print("⚠  進入測試模式 (不會實際控制燈光)")
        ser = None
else:
    print("⚠  進入測試模式 (不會實際控制燈光)")

# --- 初始化 MediaPipe ---
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def get_gesture_data(landmarks):
    """
    辨識手勢並回傳 (手勢名稱, 代碼)
    代碼: Paper=1, Rock=2, Scissors=3, Unknown=4
    """
    # 指尖 ID
    finger_tips = [8, 12, 16, 20]   # 食指, 中指, 無名指, 小指
    finger_pips = [6, 10, 14, 18]   # 指節
    
    fingers_open = []

    # 判斷拇指 (比較 X 軸)
    if abs(landmarks[4].x - landmarks[9].x) > abs(landmarks[3].x - landmarks[9].x):
        fingers_open.append(1)  # 拇指開
    else:
        fingers_open.append(0)  # 拇指關

    # 判斷四指 (比較 Y 軸)
    for tip, pip in zip(finger_tips, finger_pips):
        if landmarks[tip].y < landmarks[pip].y:
            fingers_open.append(1)  # 手指開
        else:
            fingers_open.append(0)  # 手指關

    total_open = sum(fingers_open)

    # 手勢判斷邏輯
    if total_open >= 4:  # 布
        return "Paper", 1
    elif fingers_open[1] == 1 and fingers_open[2] == 1 and fingers_open[3] == 0 and fingers_open[4] == 0:
        return "Scissors", 3  # 剪刀
    elif total_open <= 1:  # 石頭
        return "Rock", 2
    else:  # 未知
        return "Unknown", 4

def send_to_esp32(code):
    """傳送指令到 ESP32"""
    if ser and ser.is_open:
        try:
            # 傳送代碼 + 換行符號
            msg = str(code) + '\n'
            ser.write(msg.encode('utf-8'))
            # print(f"傳送: {msg.strip()}")
            return True
        except Exception as e:
            print(f"傳送失敗: {e}")
            return False
    return False

def main():
    """主程式"""
    print("=" * 50)
    print("Hand Gesture ESP32 Light Control")
    print("=" * 50)
    print("手勢對應:")
    print("  布 (Paper)    -> 代碼 1 -> 白色燈光")
    print("  石頭 (Rock)   -> 代碼 2 -> 綠色燈光")
    print("  剪刀 (Scissors)-> 代碼 3 -> 紅色燈光")
    print("  未知/無手     -> 代碼 4 -> 熄滅")
    print("按 'q' 鍵退出程式")
    print("=" * 50)
    
    cap = cv2.VideoCapture(0)
    
    # 設定解析度
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # 控制傳送頻率
    last_send_time = 0
    send_interval = 0.15  # 每 0.15 秒傳送一次
    last_code = None
    
    with mp_hands.Hands(
        model_complexity=0,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5) as hands:
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("無法讀取影像")
                continue

            # 影像處理
            image = cv2.flip(image, 1)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)
            
            # 預設值
            current_code = 4
            gesture_name = "No Hand"
            
            # 顯示狀態列
            status_color = (0, 255, 0) if ser else (0, 0, 255)
            status_text = "已連接 ESP32" if ser else "測試模式 (未連接)"
            cv2.putText(image, status_text, (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # 繪製手部關節點
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                        mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2))
                    
                    # 辨識手勢
                    gesture_name, current_code = get_gesture_data(hand_landmarks.landmark)
            
            # 顯示手勢資訊
            cv2.putText(image, f"手勢: {gesture_name}", (10, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(image, f"代碼: {current_code}", (10, 110),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # 顯示燈光狀態
            color_info = {
                1: "白色",
                2: "綠色", 
                3: "紅色",
                4: "熄滅"
            }
            cv2.putText(image, f"燈光: {color_info.get(current_code, '未知')}", (10, 150),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # 傳送指令到 ESP32
            if time.time() - last_send_time > send_interval:
                if current_code != last_code:  # 只有代碼變化時才傳送
                    if send_to_esp32(current_code):
                        last_code = current_code
                last_send_time = time.time()
            
            # 顯示視窗
            cv2.imshow('Hand Gesture Control - 按 q 退出', image)
            
            # 按 q 退出
            if cv2.waitKey(5) & 0xFF == ord('q'):
                print("\n正在關閉程式...")
                break
    
    # 清理資源
    cap.release()
    cv2.destroyAllWindows()
    
    if ser:
        ser.close()
        print("序列埠已關閉")
    
    print("程式結束")

if __name__ == "__main__":
    main()
