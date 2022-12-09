import gauss
import numpy

V = 7
n = 11
h = 0.1


def y(x):
    return V * x


def f_x(x):
    return V * ((4 * x) / 3 + (x ** 2) / 4 + (x ** 3) / 5)


def A_k_j(x, t):
    return x * t + x ** 2 * t ** 2 + x ** 3 * t ** 3


def print_table(lst1, lst2, lst3, lst4):
    s = 45
    print(f'{"x": <20}{"y метода": <20}{"y точное": <20}{"погрешность": <30}\n')

    for i in range(len(lst1)):
        print(f'{lst1[i]: <20.5f}{lst2[i]: <20.5f}{lst3[i]: <20.5f}{lst4[i]: <30.20f}')


x_h = [i / 10 for i in range(n - 1)]
y_ex = [y(x) for x in x_h]

lambda_ = 1

# СЛАУ
A = []
b = []
for k in range(n - 1):
    cur_lst = []
    for j in range(n - 1):
        if k == j:
            cur_lst.append(lambda_ * h * A_k_j(x_h[k], x_h[j]) + 1)
        else:
            cur_lst.append(lambda_ * h * A_k_j(x_h[k], x_h[j]))
    A.append(cur_lst)
    b.append(f_x(x_h[k]))

y_met = gauss.method_Gauss(A, b)

e = [abs(y_met[i] - y_ex[i]) for i in range(n - 1)]
print(f'{"Решение исходной задачи (параграф 4.2)": ^63}')
print_table(x_h, y_met, y_ex, e)
