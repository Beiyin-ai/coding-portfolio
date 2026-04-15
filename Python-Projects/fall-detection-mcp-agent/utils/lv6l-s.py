#!/usr/bin/python3

# echo $XDG_SESSION_TYPE

# https://github.com/ponty/pyscreenshot
# python3 -m pip install Pillow pyscreenshot

import numpy as np
import pyscreenshot as ImageGrab
import socket
import struct
import time
import lzma
from screeninfo import get_monitors
import argparse

bind_IP = '234.3.2.1'
bind_Port = 6502

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--monitor", help="分享那個螢幕 ( 預設＝0 表示全部 )", type=int, default = 0)
args = parser.parse_args()
monitor = args.monitor
if monitor >0 :
    mons=get_monitors()
    if monitor > len(mons) : 
        monitor = len(mons)
    monDoc = mons[ monitor -1 ]
    bbox=( monDoc.x , monDoc.y , monDoc.x + monDoc.width , monDoc.y + monDoc.height )
else :
    bbox = None

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

ttl = 7
sender.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack('@i', ttl ) )

sender.settimeout(0.2) # Set a timeout so the socket does not block indefinitely when trying to receive data.
packMaxSize = 65400
packSize = packMaxSize
b_packMaxSize = packSize.to_bytes(2,'big')
b_RGB = int(3).to_bytes(1,'big')

cnt=1
errcnt=0
serving = True
while serving:
    img = ImageGrab.grab(bbox=bbox, backend="pil", childprocess=False)
    total = img.width * img.height * 3
    pksum = img.height
    packSize = img.width * 3
    b_packMaxSize = packSize.to_bytes(2,'big')
    head = b_packMaxSize + int(time.time()*100).to_bytes(5,'big') + b_RGB + img.height.to_bytes(2,'big') + img.width.to_bytes(2,'big') 
    img_bytes = img.tobytes()
    for ii in range( pksum ) :
        pk_offset = ii * packSize
        try:
            z_mm = lzma.compress( head + ii.to_bytes(2,'big') + img_bytes[ pk_offset : pk_offset + packSize ] )
            sender.sendto( z_mm , (bind_IP, bind_Port))
        except KeyboardInterrupt:
            print(' End program : 鍵盤 Ctrl-C 中斷')
            serving = False
            break
        except Exception as e:
            errcnt +=1
            print( f'End program : Exception, {e}' )
        except SystemExit as e:
            errcnt +=1
            print(f'End program : SystemExit, {e}')
        except :
            errcnt +=1
            print('End program : Some Error')
    
    print( errcnt, cnt )
    cnt +=1

if isinstance( sender , socket.socket ) : sender.close()