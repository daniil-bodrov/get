




import time
import RPi.GPIO as GPIO
import r2r_adc
import adc_plot
vv = []
tv = []
dur = 13.0


if __name__ == "__main__":
    try:
        start_time = time.time()
        d = 0
        dac = r2r_adc.R2R_ADC(3.183, compare_time = 0.001)
        while time.time() - dur < start_time:
            try:
                voltage = dac.get_voltage()
                if voltage > 0:
                    vv.append(voltage)
                    tv.append(time.time() - start_time)
                print(voltage)
            except ValueError:
                print("Вы не ввели число. Попробуйте еще раз")
        adc_plot.plot_voltage_vs_time(tv, vv, 3.183)
        adc_plot.plot_sampling_period_hist(tv)
    finally:
        dac.deinit()