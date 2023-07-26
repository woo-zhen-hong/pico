from machine import *
from pico_i2c_lcd import *

i2c = I2C(1, sda=Pin(14), scl=Pin(15))
print(i2c.scan())
