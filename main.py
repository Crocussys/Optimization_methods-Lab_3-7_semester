import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def f(x):
    return x ** 5 - 7 * x ** 3 + x - 1


def half_division(func, a, b, eps):
    i = 0
    while b - a > 3 * eps:
        temp = (a + b) / 2
        print(f"Итерация {i}: [{a}, {b}]")
        p = temp - eps
        q = temp + eps
        if func(p) < func(q):
            b = q
        else:
            a = p
        i += 1
    print(f"Ответ: {(a + b) / 2}\n")


def golden_ratio(func, a, b, eps):
    fe = (1 + math.sqrt(5)) / 2
    i = 0
    while abs(b - a) >= eps:
        print(f"Итерация {i}: [{a}, {b}]")
        x1 = b - (b - a) / fe
        x2 = a + (b - a) / fe
        if func(x1) >= func(x2):
            a = x1
        else:
            b = x2
        i += 1
    print(f"Ответ: {(a + b) / 2}\n")


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
    show_chart(f, -5, 5, -25, 25)
    xl = 1
    xr = 3
    print(f"Выбранный отрезок: [{xl}, {xr}]\n")
    for e in [0.1, 0.01, 0.001, 1e-06]:
        print(f"------Epsilon = {e}------")
        print("Метод половинного деления")
        half_division(f, xl, xr, e)
        print("Метод золотого сечения")
        golden_ratio(f, xl, xr, e)
