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
    v = 10**-3
    p = R * T / (v - b) - a / v ** 2


b = 3.19 * 10 ** -5
P(-130, 8.314, 0.1382, b)
plt.plot(V_list, P_list)


def minSearch(X, Y, eps): # этот ужас я доделаю
    a = 0
    b = len(X) - 1
    x1 = (a + b - eps) / 2
    x2 = (a + b + eps) / 2
    flag1 = False
    flag2 = False
    for i in range(len(X)):
        if i >= x1 and flag1 == False:
            flag1 = True
            x1 = i
        if i >= x2 and flag2 == False:
            flag2 = True
            x2 = i
            break

    while x2 - x1 > eps:
        if Y(X[x1]) <= Y(X[x2]):
            b = x2
        else:
            a = x1
        x1 = (a + b - eps) / 2
        x2 = (a + b + eps) / 2
        flag1 = False
        flag2 = False
        for i in range(len(X)):
            if i >= x1 and flag1 == False:
                flag1 = True
                x1 = i
            if i >= x2 and flag2 == False:
                flag2 = True
                x2 = i
                break



    # plt.scatter(x1, Y(X[x1]), color='red')

    print(X[x1])


def Y(v):
    R = 8.314
    a = 0.1382
    b = 3.19 * 10 ** -5
    T = -130 + 273.15
    return R * T / (v - b) - a/v**2


eps = (pow(10, -3) - (b + pow(10, -5))) / 1000
minSearch(V_list, P_list, eps)

plt.show()
