
import time
import RPi.GPIO as GPIO
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.bits_gpio = [26,20,19,16,13,12,25,11]
        self.comp_gpio = 21
        self.compare_time = compare_time
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        if number < 0:
            a = [0,0,0,0,0,0,0,0]
        elif number <= 255:
            a = [int(el) for el in reversed(bin(number)[2:].zfill(8))]
        else:
            a = [1,1,1,1,1,1,1,1]
        print(a)
        GPIO.output(self.bits_gpio, a)
    def gvoltage(self):
        if not(0.0 <= voltage <= self.dynamic_range):
            return 0

        nuu = int(voltage/self.dynamic_range * 255)
        print(self.dynamic_range)
        nu = self.set_number(nuu)
        return nu
    def sequential_counting_adc(self):
        v = 0
        self.number_to_dac(v)
        while not(GPIO.input(self.comp_gpio)) and v <= 255:
            self.number_to_dac(v)
            v += 1

            time.sleep(0.01)
        return v
    def get_voltage(self):
        bruh = self.sequential_counting_adc()
        return self.dynamic_range*bruh/255
    
    def suc_approx(self):
        GPIO.output(self.bits_gpio, 0)
        bv = [0]*8
        for i in range(8):
            bv[i] = 1
            GPIO.output(self.bits_gpio, bv)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                bv[i] = 0
        return int(''.join(list(map(str, bv))), 2)
    def svolt(self):
        bruh = self.suc_approx()
        return self.dynamic_range*bruh/255



if __name__ == "__main__":
    try:
        d = 0
        dac = R2R_ADC(3.183)
        while True:
            try:
                #voltage = dac.get_voltage()
                voltage = dac.svolt()
                print(voltage)
            except ValueError:
                print("Вы не ввели число. Попробуйте еще раз")
    finally:
        dac.deinit()