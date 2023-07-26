from machine import *
from utime import *

class Servo:
    def __init__(self, pin, reset=False):
        self.servo = PWM(Pin(pin))
        self.servo.freq(50)
        if reset:
            self.rotate(0)
        
    def rotate(self, degree, delay=0.4):
        self.degree = degree
        dc = (0.12 - 0.025) / 180 * degree + 0.025
        self.servo.duty_u16(int(65535 * dc))
        sleep(delay)
        
    def close(self):
        self.servo.deinit()

if __name__ == '__main__':
    servo = Servo(16, False)
    servo.rotate(150)
    servo.close()