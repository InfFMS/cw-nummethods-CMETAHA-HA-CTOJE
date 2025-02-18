import matplotlib.pyplot as plt


def P_1(T, R, a, b):  # функция чтобы рисовать график
    T += 273.15
    global X, Y
    X, Y = [], []
    v = b + 10**-5
    while v < 10**-3:
        X.append(v)
        p = R * T / (v - b) - a/v**2
        Y.append(p)
        v += (pow(10, -3) - (b + pow(10, -5))) / 10000
    v = 10**-3
    X.append(v)
    p = R * T / (v - b) - a / v ** 2
    Y.append(p)



b = 3.19 * 10 ** -5
P_1(-130, 8.314, 0.1382, b)
plt.plot(X, Y)


def minSearch(X, eps):  # функция рисует точку минимума
    a = 0
    b = round((len(X) - 1) / 6)     # рассматривается первая шестая часть множества аргументов, иначе ищет минимум не там, где надо
    x1 = round((a + b - eps) / 2)
    x2 = round((a + b + eps) / 2)
    while b - a > 2*eps:
        if P(X[x1]) <= P(X[x2]):
            b = x2
        else:
            a = x1
        x1 = round((a + b - eps) / 2)
        x2 = round((a + b + eps) / 2)
    plt.scatter(X[x1], P(X[x1]), color='blue')
    return X[x1]

def maxSearch(X, eps): # функция рисует точку максимума
    a = 0   # от нулевого аргумента (нулевого числа в массиве X)
    b = round((len(X) - 1) / 6)     # рассматривается первая шестая часть множества аргументов, иначе ищет минимум не там, где надо
    x1 = round((a + b - eps) / 2)
    x2 = round((a + b + eps) / 2)
    while b - a > 2*eps:
        if P(X[x1]) >= P(X[x2]):
            b = x2
        else:
            a = x1
        x1 = round((a + b - eps) / 2)
        x2 = round((a + b + eps) / 2)
    plt.scatter(X[x1], P(X[x1]), color='red')
    return X[x1]



def P(V):   # функция возвращает значение P(v)
    R = 8.314
    a = 0.1382
    b = 3.19 * 10 ** -5
    T = -130 + 273.15
    return R * T / (V - b) - a/V**2


def drawGraph(func, a, b):
    global X, Y
    X, Y = [], []
    x = a
    while x < b:
        X.append(x)
        Y.append(func(x))
        x += (b - a) / 10000
    X.append(b)
    Y.append(func(b))

b = 3.19 * 10 ** -5
drawGraph(P, b + 10 ** -5, 10 ** -3)


eps = 1     # точность до одного шага итерации (одного числа в массиве X)
minSearch(X, eps)
maxSearch(X, eps)
plt.show()
