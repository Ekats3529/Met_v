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



import gauss

V = 7
n = 3
h = 0.1


def y(x):
    return V * x


def f_x(x):
    return V * ((4 * x) / 3 + (x ** 2) / 4 + (x ** 3) / 5)


def a_i(x, i):
    return x ** i


def b_i(t, i):
    return t ** i


def print_table(lst1, lst2, lst3, lst4):
    s = 45
    print(f'{"x": <20}{"y метода": <20}{"y точное": <20}{"погрешность": <30}\n')

    for i in range(len(lst1)):
        print(f'{lst1[i]: <20.5f}{lst2[i]: <20.5f}{lst3[i]: <20.5f}{lst4[i]: <30.20f}')


x_h = [i / 10 for i in range(10)]
y_ex = [y(x) for x in x_h]

lst_A = [[1 / (i + k + 1) for k in range(1, n + 1)] for i in range(1, n + 1)]

lst_phi = [28 / 9 + 7 / 16 + 7 / 25, 7 / 3 + 7 / 20 + 7 / 30, 28 / 15 + 7 / 24 + 1 / 5]

# СЛАУ
A = []
b = []
for k in range(n):
    cur_lst = []
    for i in range(n):
        if k == i:
            cur_lst.append(lst_A[i][k] + 1)
        else:
            cur_lst.append(lst_A[i][k])
    A.append(cur_lst)
    b.append(lst_phi[k])

lst_q = gauss.method_Gauss(A, b)

y_met = []
for k in range(len(x_h)):
    cur_sum = 0
    for i in range(n):
        cur_sum += lst_q[i] * a_i(x_h[k], i + 1)
    y_met.append(f_x(x_h[k]) - cur_sum)

e = [abs(y_met[i] - y_ex[i]) for i in range(len(x_h))]
print(f'{"Решение исходной задачи (параграф 4.1)": ^63}')
print_table(x_h, y_met, y_ex, e)
