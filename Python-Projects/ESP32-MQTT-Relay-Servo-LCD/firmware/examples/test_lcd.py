from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
import time

i2c = I2C(1, freq=400000)
I2C_LCD = 0x27

lcd = I2cLcd(i2c, I2C_LCD, 2, 16)

print( f"i2c.scan()->{ i2c.scan() }")

lcd.backlight_on()

lcd.clear()

try:
    while True:
        cst = time.localtime(time.mktime(time.localtime()) + 28800)
        ay="{0}/{1:02d}/{2:02d} {3:02d}:{4:02d}:{5:02d}".format( *cst ).split(' ')
        lcd.move_to(0, 0)
        lcd.putstr("Date: {}\nTime: {}".format(*ay))
        time.sleep(1)
except Exception as e: print(e)