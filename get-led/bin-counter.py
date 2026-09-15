import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [24,22,23,27,17,25,12,16]
GPIO.setup(leds, GPIO.OUT)
num = 0
button1 = 9
button2 = 10
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.output(leds, 0)
def dec2bin(va):
    return [int(el) for el in bin(va)[2:].zfill(8)]

while True:
    if GPIO.input(button1):
        num += 1
        if num > 127:
            num = 127
        print(num, dec2bin(num))
        time.sleep(0.2)
    if GPIO.input(button2):
        num -= 1
        if num < 0:
            num = 0
        print(num, dec2bin(num))
        time.sleep(0.2)
    GPIO.output(leds, dec2bin(num))
    
    
