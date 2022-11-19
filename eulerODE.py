import numpy as np
import matplotlib.pyplot as plt

def base_ODE(t, x):

    dxdt = x*np.sin(t)

    return dxdt

def cul_ODE(t0, x0, h, n):
    tList = []
    xList = []
    t_temp = t0
    x_temp = x0
    tList.append(t_temp)
    xList.append(x_temp)
    for i in range(n):
        t_temp = t_temp + h
        x_temp = x_temp + h*base_ODE(t_temp, x_temp)
        tList.append(t_temp)
        xList.append(x_temp)

    return tList, xList

def plot_ODE(t, x):
    fig = plt.figure()
    sbfig = fig.add_subplot(1, 1, 1)
    sbfig.plot(t, x)
    plt.show()

N = 1000
H = 0.1
T0 = 0.0
X0 = 1.0

T, X = cul_ODE(T0, X0, H, N)
plot_ODE(T, X)