import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def f(x):
    return x ** 5 - 7 * x ** 3 + x - 1


def half_division(func, a, b, eps):
    while b - a > 3 * eps:
        temp = (a + b) / 2
        print(temp)
        p = temp - eps
        q = temp + eps
        if func(p) < func(q):
            a = q
        else:
            a = p
    print((a + b) / 2)
    return (a + b) / 2


def golden_ratio(func, a, b, eps):
    fe = (1 + math.sqrt(5)) / 2
    while abs(b - a) >= eps:
        print((a + b) / 2)
        x1 = b - (b - a) / fe
        x2 = a + (b - a) / fe
        if func(x1) >= func(x2):
            a = x1
        else:
            b = x2
    print((a + b) / 2)
    return (a + b) / 2


def show_chart(func, x0, x1, y0, y1, delta=100):
    x_all = [i / delta for i in range(x0 * delta, x1 * delta + 1)]
    fig, ax = plt.subplots()
    ax.plot(x_all, list(map(func, x_all)), label="График")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.grid(which='major', color='gray', linestyle=':')
    ax.legend()
    plt.xlim([x0, x1])
    plt.ylim([y0, y1])
    plt.ylabel("y", fontsize=14)
    plt.xlabel("x", fontsize=14)
    plt.savefig("chart.svg")
    plt.show()


if __name__ == '__main__':
    xl = 1
    xr = 3
    e = 0.1
    show_chart(f, -10, 10, -25, 25)
    half_division(f, xl, xr, e)
    golden_ratio(f, xl, xr, e)
