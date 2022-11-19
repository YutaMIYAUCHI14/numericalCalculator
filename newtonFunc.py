import numpy as np

def base_func(t):

    function = t**2 - 5

    return function

def diff_func(t):

    diffFunction = 2*t

    return diffFunction

def cul_func(t0, n):
    t_temp = t0
    f_temp = base_func(t0)
    df_temp = diff_func(t0)
    for i in range(n):
        t_temp = t_temp - f_temp/df_temp
        f_temp = base_func(t_temp)
        df_temp = diff_func(t_temp)

    return t_temp

N = 100
T0 = 50
print("推定値:")
print(cul_func(T0, N))
print("真値:")
print(np.sqrt(5))