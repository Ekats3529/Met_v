import gauss

V = 7
x_0 = 0
x_T = V
y_0 = 0
y_T = 0
h = 0.5
eps = 1e-9


def y(x):
    return x ** 3 - V * x ** 2


def f(x):
    return 4 * x ** 4 - 3 * V * x ** 3 + 6 * x - 2 * V


def p(x):
    return x ** 2


def q(x):
    return x


def coef_y_k_min_1(x):
    return 1 / (h ** 2) - p(x) / (2 * h)


def coef_y_k(x):
    return -2 / (h ** 2) + q(x)


def coef_y_k_plus_1(x):
    return 1 / (h ** 2) + p(x) / (2 * h)


def print_table(lst1, lst2, lst3, lst4):
    s = 45
    print(f'{"x": <15}{"y метода": <15}{"y точное": <15}{"погрешность": <15}\n')

    for i in range(len(lst1)):
        print(f'{lst1[i]: <15.4f}{lst2[i]: <15.4f}{lst3[i]: <15.4f}{lst4[i]: <15.4f}')


lft = 0
rgt = V
x_h = [x_0]
y_ex = [y_0]
n = int(rgt / h)

x = lft
while x < rgt - eps:
    x_h.append(x + h)
    y_ex.append(y(x + h))
    x += h

# СЛАУ


cur_lst = [1] + [0] * n

A = [cur_lst]   # первая строка матрицы A - коэф. 1 при y_0 и 0 при остальных y
b = [0]     # первое значение столбца b равно 0

for k in range(1, n):
    cur_lst = [0] * (n + 1)
    cur_lst[k - 1] = coef_y_k_min_1(x_h[k])
    cur_lst[k] = coef_y_k(x_h[k])
    cur_lst[k + 1] = coef_y_k_plus_1(x_h[k])
    A.append(cur_lst)
    b.append(f(x_h[k]))

cur_lst = [0] * n + [1]
A.append(cur_lst)  # последняя строка матрицы A - коэф. 1 при y_n и 0 при остальных y
b.append(0)  # последнее значение столбца b равно 0

y_dif = gauss.method_Gauss(A, b)
e = [abs(y_dif[i] - y_ex[i]) for i in range(n + 1)]

print(f'{"Разностный метод": ^63}\n')
print_table(x_h, y_dif, y_ex, e)




