



import time
import RPi.GPIO as GPIO
import adc_plot
import mcp3021_driver
vv = []
tv = []
d = 6.0
dac = mcp3021_driver.MCP3021(3.183)
try:
    st = time.time()
    while time.time() - d < st:
        v = dac.get_voltage()
        if v > 0:
            vv.append(v)
            tv.append(time.time()-st)
    adc_plot.plot_voltage_vs_time(tv, vv, 3.183)
    adc_plot.plot_sampling_period_hist(tv)
finally:
    dac.deinit()