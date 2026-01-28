"""
Utility functions for the hand gesture project
"""

import serial
import serial.tools.list_ports

def get_available_serial_ports():
    """取得所有可用的序列埠"""
    ports = serial.tools.list_ports.comports()
    port_list = []
    
    for port in ports:
        port_info = {
            'device': port.device,
            'description': port.description,
            'hwid': port.hwid,
            'vid': port.vid if port.vid else 'N/A',
            'pid': port.pid if port.pid else 'N/A'
        }
        port_list.append(port_info)
    
    return port_list

def print_serial_ports():
    """列印可用的序列埠資訊"""
    ports = get_available_serial_ports()
    
    if not ports:
        print("未找到任何序列埠")
        return
    
    print("可用的序列埠:")
    print("-" * 80)
    for i, port in enumerate(ports, 1):
        print(f"{i}. {port['device']}")
        print(f"   描述: {port['description']}")
        print(f"   VID:PID: {port['vid']}:{port['pid']}")
        print(f"   HWID: {port['hwid']}")
        print()

def test_serial_connection(port, baudrate=9600):
    """測試序列埠連線"""
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        ser.close()
        return True
    except:
        return False
