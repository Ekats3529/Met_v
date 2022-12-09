from math import sqrt


def f(x1, x2):
    return 132 * x1 ** 2 - 115 * x1 * x2 + 132 * x2 ** 2 - 51 * x1 - 135 * x2 + 49


def delta_f(x1, x2):
    f_x1 = 264 * x1 - 115 * x2 - 51
    f_x2 = 264 * x2 - 115 * x1 - 135
    return f_x1, f_x2


def norm(d_f):
    return sqrt(d_f[0] ** 2 + d_f[1] ** 2)


def gradient(eps, alpha, x):
    f_x = f(x[0], x[1])
    d_f = delta_f(x[0], x[1])

    while norm(d_f) > eps:
        y = [x[0] - alpha * d_f[0], x[1] - alpha * d_f[1]]
        f_y = f(y[0], y[1])
        if f_y < f_x:
            x = y
            f_x = f_y
        else:
            alpha /= 2
        d_f = delta_f(x[0], x[1])
    print(f"({x[0]}, {x[1]})")


eps = 0.0001
alpha = 1
x = [1, 1]
gradient(eps, alpha, x)
