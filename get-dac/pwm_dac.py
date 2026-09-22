import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    def set_voltage(self, voltage):
        if not(0.0 <= voltage <= self.dynamic_range):
            return 0

        nu = int(voltage/self.dynamic_range * self.pwm_frequency)
        return nu
    
if __name__ == "__main__":
    try:
        d = 0
        dac = PWM_DAC(12, 500, 3.183, True)
        pwm = GPIO.PWM(dac.gpio_pin, dac.pwm_frequency)
        pwm.start(d)
        while True:
            try:
                voltage = float(input("Введите напряжене в Вольтах: "))
                d = dac.set_voltage(voltage)
                d //= 5
                pwm.ChangeDutyCycle(d)
                print(d)
                GPIO.output(dac.gpio_pin, d)
            except ValueError:
                print("Вы не ввели число. Попробуйте еще раз")
    finally:
        dac.deinit()