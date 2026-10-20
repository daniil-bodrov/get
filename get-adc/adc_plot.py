
import matplotlib.pyplot as plt


def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("grafic of dumb voltage on adc")
    plt.xlabel("time, s")
    plt.ylabel("voltage, v")
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(t):
    sp = []
    for i in range(len(t) - 1):
        sp.append(t[i+1]-t[i])
    plt.figure(figsize=(10,6))
    plt.hist(sp)
    plt.title("grafic of dumb discretisation times of times on adc")
    plt.xlabel("time, s")
    plt.ylabel("times")
    #plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()