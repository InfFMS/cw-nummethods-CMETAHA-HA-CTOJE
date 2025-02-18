import matplotlib.pyplot as plt

def P(T, R, a, b):
    T += 273.15
    global V_list, P_list
    V_list, P_list = [], []
    v = b + 10**-5
    while v < 10**-3:
        V_list.append(v)
        p = R * T / (v - b) - a/v**2
        P_list.append(p)
        v += (pow(10, -3) - (b + pow(10, -5))) / 10000
    v = 10 ** -3
    p = R * T / (v - b) - a / v ** 2

b = 3.19 * 10 ** -5

P(-140, 8.314, 0.1382, b)
plt.plot(V_list, P_list, label='T = -140°C')

P(-130, 8.314, 0.1382, b)
plt.plot(V_list, P_list, label='T = -130°C')

P(-120, 8.314, 0.1382, b)
plt.plot(V_list, P_list, label='T = -120°C')

P(-110, 8.314, 0.1382, b)
plt.plot(V_list, P_list, label='T = -110°C')

P(-100, 8.314, 0.1382, b)
plt.plot(V_list, P_list, label='T = -100°C')

plt.legend()
plt.show()
