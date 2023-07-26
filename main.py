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

# 初始化內建LED
#internal_led = Pin("LED", Pin.OUT)
#external_led = Pin(20, Pin.OUT)

# 初始化LCD
I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(1, sda=Pin(14), scl=Pin(15))
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.hide_cursor()

# 初始化LED燈條
numpix = 8
state_machine = 0
pin = 0
np = Neopixel(numpix, state_machine, pin, 'GRB')
np.clear()
np.show()

# 初始化舵機
servo = mservo.Servo(16, True)

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
    year = crime.year[0:3]
    month = crime.month
    crimetype = crime.type
    happen = crime.happen
    clear = crime.clear
    lcd.clear()
    lcd.putstr('{} {} {}'.format(year, month, crimetype[0:1]))
    lcd.putstr('\n{} {}'.format(happen, clear))
    # 調整舵機角度
    servo.rotate(190 - (int(crime.percent[0:2]) / 100 * 190))

### LED燈條顯示溫度
#def setLEDStrip(color, value, brightness=10):
    #np.clear()
    #if value < 10:
        #np.set_pixel_line(0, 0, color, brightness)
    #elif value < 20:
        #np.set_pixel_line(0, 1, color, brightness)
    #elif value < 25:
        #np.set_pixel_line(0, 2, color, brightness)
    #elif value < 28:
        #np.set_pixel_line(0, 3, color, brightness)
    #elif value < 30:
        #np.set_pixel_line(0, 4, color, brightness)
    #elif value < 33:
        #np.set_pixel_line(0, 5, color, brightness)
    #elif value < 36:
        #np.set_pixel_line(0, 6, color, brightness)
    #else:
        #np.set_pixel_line(0, 7, color, brightness)
    #np.show()

#setLEDStrip((0,255,255), int(weather.minT))

#isHigh = False
showCrime()
while True:
    if button.value() == 1:
        index += 1
        showCrime()
        #external_led.on()
        #isHigh = not isHigh
        #if isHigh:
            #setLEDStrip((255,0,0), int(weather.maxT))
        #else:
            #setLEDStrip((0,255,255), int(weather.minT))      
    sleep(0.5)
    #external_led.off()


