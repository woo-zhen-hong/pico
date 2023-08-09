import mwifi
import mcrime
import mservo
import mstorage
import _thread
from machine import *
from pico_i2c_lcd import *
from mneopixel import *
from utime import *

# WiFi name
SSID = ''
# WiFI password
PASSWORD = ''
# data URL
URL = 'https://api.kcg.gov.tw/api/service/get/99c8d84a-3553-4fe7-8321-f2f85c7a7715'

# 初始化LCD
I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(1, sda=Pin(14), scl=Pin(15))
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.hide_cursor()

# 初始化舵機
servo = mservo.Servo(16, True)
servo.rotate(190)

# 初始化按鈕
button = Pin(4, Pin.IN, Pin.PULL_DOWN)
# 初始化資料位置
index = 0

# 連線 Wi-Fi
mwifi.Wifi(SSID, PASSWORD)
lcd.putstr('Wi-Fi connected')

# 取得犯罪資訊
def showCrime():
    crime = mcrime.Crime(index, url=URL)
    crime.info()
    # LCD顯示年度、月份、案件別、發生數、破獲數
    year = crime.year[0:4]
    month = crime.month
    crimetype = crime.type
    happen = crime.happen
    clear = crime.clear
    lcd.clear()
    lcd.putstr('{} {} {}\n'.format(year, month, crimetype[0]))
    if (crime.percent[2] == '.'):
        lcd.putstr('{} {} {}%'.format(happen, clear, crime.percent[0:2]))
        # 調整舵機角度
        servo.rotate(190 - (int(crime.percent[0:2]) / 100 * 190))
    else:
        lcd.putstr('{} {} {}%'.format(happen, clear, 100))
        # 調整舵機角度
        servo.rotate(190 - (100) / 100 * 190)

showCrime()
while True:
    if button.value() == 1:
        index += 1
        showCrime()    
    sleep(0.1)



