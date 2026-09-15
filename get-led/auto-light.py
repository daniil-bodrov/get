import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)
sun = 6
GPIO.setup(sun, GPIO.IN)
state = 0
period = 1.0
while True:
    d = 1 - GPIO.input(sun)
    GPIO.output(led, d)
    time.sleep(0.2)