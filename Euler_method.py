V = 7
x_0 = V
y_0 = 0
h = 0.1
lft = V
rgt = V + 5
eps = 1e-9


def y(x):
    return x ** 4 - V * x ** 3


def f(x, y):
    return 4 * x ** 3 - 3 * V * x ** 2


def y_k_euler(x_k, y):
    return y + h * f(x_k, y)


def y_k_euler_improved(x_k, y_k):
    return y_k + h * f(x_k + h / 2, y_k + h / 2 * f(x_k, y_k))


def y_k_correct(x_k, x_k_1, y_k):
    return y_k + (h / 2) * (f(x_k, y_k) + f(x_k_1, y_k + h * f(x_k, y_k)))


def print_table(lst1, lst2, lst3, lst4):
    s = 45
    print(f'{"x": <15}{"y метода": <15}{"y точное": <15}{"погрешность": <15}\n')

    for i in range(len(lst1)):
        print(f'{lst1[i]: <15.4f}{lst2[i]: <15.4f}{lst3[i]: <15.4f}{lst4[i]: <15.4f}')


x_h = [x_0]
y_x = [y_0]

# метод Эйлера
y_euler = [y_0]
eps_eul_met = [abs(y_x[0] - y_euler[0])]

# Усовершенствованный метод Эйлера
y_euler_improved = [y_0]
eps_eul_improved = [abs(y_x[0] - y_euler_improved[0])]

# Метод предварительного и корректирующего счета
y_cor = [y_0]
eps_cor = [abs(y_x[0] - y_cor[0])]

x = lft
k = 1
while x < rgt - eps:
    x_h.append(x + h)
    y_x.append(y(x + h))

    # метод Эйлера
    y_euler.append(y_k_euler(x_h[k - 1], y_euler[k - 1]))
    eps_eul_met.append(abs(y_x[k] - y_euler[k]))

    # Усовершенствованный метод Эйлера
    y_euler_improved.append(y_k_euler_improved(x_h[k - 1], y_euler_improved[k - 1]))
    eps_eul_improved.append(abs(y_x[k] - y_euler_improved[k]))

    # Метод предварительного и корректирующего счета
    y_cor.append(y_k_correct(x_h[k - 1], x_h[k], y_cor[k - 1]))
    eps_cor.append(abs(y_x[k] - y_cor[k]))

    x += h
    k += 1

print(f'{"Метод Эйлера": ^63}\n')
print_table(x_h, y_euler, y_x, eps_eul_met)
print()

print(f'{"Усовершенствованный метод Эйлера": ^63}\n')
print_table(x_h, y_euler_improved, y_x, eps_eul_improved)
print()

print(f'{"Метод предварительного и корректирующего счета": ^63}\n')
print_table(x_h, y_cor, y_x, eps_cor)
