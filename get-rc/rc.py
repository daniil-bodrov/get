



import time
import smbus

import RPi.GPIO as GPIO
class MCP3021:
    def __init__(self, dr, address=0x4D, verbose = True):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.verbose = verbose
        self.dr = dr
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)

        if self.verbose:
            print(f"принято: {data}, старший байт: {upper_data_byte:x}, младший байт: {lower_data_byte:x}, число: {number}")
        return number
    def get_voltage(self):
        bruh = self.get_number()
        return self.dr * bruh / 1024




if __name__ == "__main__":
    try:
        dac = MCP3021(3.2)
        while True:
            try:
                voltage = dac.get_voltage()
                print(voltage)
                time.sleep(0.1)
                
                #print(nu)
            except ValueError:
                print("Вы не ввели число. Попробуйте еще раз")
    finally:
        dac.deinit()