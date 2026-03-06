#from machine import Pin, I2C
from machine import Pin, PWM
import time, network, ntptime
from umqtt.robust import MQTTClient
#from machine_i2c_lcd import I2cLcd

WiFi_ssid = "aiot3"
WiFi_password = "aiot1234"

mqtt_broker = '123.192.211.135'
mqtt_port   = 80

mqtt_client_id = 'aiot3esp32-xx-0001'
topic_head  = b'robert/AIoTxx'

topic_all   = topic_head + b'/#'
topic_servo = topic_head + b'/servo'
topic_lcd   = topic_head + b'/LCD'
topic_relay = topic_head + b'/relay'

ntptime.host='tw.pool.ntp.org' 
GPIO_relay = Pin( 12, Pin.OUT)
GPIO_led = Pin( 2, Pin.OUT)
count = 360
cycleLen = 240
direction = 0

#i2c = I2C(1, freq=400000)
#I2C_LCD = 0x27
#I2C_arduino = 0x11
#print( f"i2c.scan()->{ i2c.scan() }")
#lcd = I2cLcd(i2c, I2C_LCD, 2, 16)
#lcd.backlight_on()
#lcd.clear()
d_min = 1638
d_span = 7864 - d_min
wifi= network.WLAN(network.STA_IF)
wifi.active(True)

pwm = PWM( Pin( 4 ) , freq = 50, duty=0 )
def mesg_come(topic, msg):
    print((topic, msg))
    if topic == topic_servo:
       try:
         nn = int(msg)
       except:
         nn = -1       
       if nn >=0 and nn < 181:          
          pwm.duty_u16( d_min + d_span * nn //180 )
#    elif topic == topic_lcd:
#       lcd.clear()
#       lcd.move_to(0, 0)
#       lcd.putstr( msg.decode() )
#    elif topic == topic_relay:
#       if ( msg == b'H' ): GPIO_relay.value( 1 )
#       elif  ( msg == b'L' ): GPIO_relay.value( 0 )

def utc_cst():
    cst = time.localtime(time.mktime(time.localtime()) + 28800)
    return "{0}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:02d}".format( *cst )

def setTime():
    try:
        print("Setting time ...")
        ntptime.settime()
    except Exception as e: 
        print(e)
    print( f"localtime->{ utc_cst() }")

try:
    wifi.connect( WiFi_ssid , WiFi_password )
    print('start to connect wifi')
    for i in range(20):
        print('try to connect wifi in {}s'.format(i))
        time.sleep(1)
        if wifi.isconnected():
            print('WiFi connection OK!')
            print('Network Config=',wifi.ifconfig())
            break          
    if not wifi.isconnected():
        print('WiFi connection Error')      
        raise Exception('WiFi connection Error')

    setTime()   
    mqttClient = MQTTClient( mqtt_client_id, mqtt_broker, port=mqtt_port, keepalive= 65535  )
    mqttClient.connect( False ) # 連線時採用 False 不清除會談資料, True 會清除會談資訊, 也就是當成全新的用戶端 
    mqttClient.set_callback( mesg_come )
    mqttClient.subscribe(topic= topic_all ) 
    old_tkms=0
    while 1:
        for j in range( count ) : 
            for i in range( cycleLen ) :
                GPIO_led.value( direction ^ ( 0 if j >= i else 1 ) )
            prn_log = mqttClient.check_msg()
            if prn_log: print( prn_log )
        direction = ~direction & 1
        print( f"localtime->{ utc_cst() }")
except Exception as e: print(e)

pwm.deinit()