


import numpy as np
import time
import RPi.GPIO as GPIO
import adc_plot
import mcp3021_driver

vv = []
tv = []
d = 15.0
dac = mcp3021_driver.MCP3021(3.183)
try:
    st = time.time()
    while time.time() - d < st:
        v = dac.get_voltage()
        if v > 0:
            vv.append(v)
            tv.append(time.time()-st)
    data = np.column_stack((tv, vv))
    np.savetxt('data.csv', data, delimiter = ' ', fmt = '%.4f', header = 'Время  [c], Напряжение[В]', comments ='', encoding = 'utf-8')
    adc_plot.plot_voltage_vs_time(tv, vv, 3.183)
    adc_plot.plot_sampling_period_hist(tv)
finally:
    dac.deinit()