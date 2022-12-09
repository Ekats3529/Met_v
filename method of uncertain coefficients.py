import gauss
import numpy

V = 7
x_0 = 0
x_T = V
y_0 = 0
y_T = 0
n = 10
eps = 1e-9


def y(x):
    return x ** 3 - V * x ** 2


def f(x):
    return 4 * x ** 4 - 3 * V * x ** 3 + 6 * x - 2 * V


def p(x):
    return x ** 2


def q(x):
    return x


# фи в точке икс
def fi_k(x, k):
    return x ** k * (x - V)


# фи штрих в точке икс
def fi_k_prime(x, k):
    return k * x ** (k - 1) * (x - V) + x ** k


# фи два штриха в точке икс
def fi_k_double_prime(x, k):
    return k * (k - 1) * x ** (k - 2) * (x - V) + 2 * k * x ** (k - 1)


def print_table(lst1, lst2, lst3, lst4):
    s = 45
    print(f'{"x": <20}{"y метода": <20}{"y точное": <20}{"погрешность": <30}\n')

    for i in range(len(lst1)):
        print(f'{lst1[i]: <20.5f}{lst2[i]: <20.5f}{lst3[i]: <20.5f}{lst4[i]: <30.20f}')


lft = 0
rgt = V
h = (rgt - lft) / (n + 1)
x_h = [x_0 + i * h for i in range(n + 2)]
y_ex = [y(x) for x in x_h]


# СЛАУ
A = []
b = []

for j in range(1, n + 1):
    cur_lst = []
    for k in range(1, n+1):
        cur_sum = fi_k_double_prime(x_h[j], k) + p(x_h[j]) * fi_k_prime(x_h[j], k) + q(x_h[j]) * fi_k(x_h[j], k)
        cur_lst.append(cur_sum)
    A.append(cur_lst)
    b.append(f(x_h[j]))

sol = gauss.method_Gauss(A, b)

y_met = []
for i in range(len(sol) + 1):
    cur_sum = 0
    for k in range(1, n + 1):
        cur_sum += sol[k - 1] * fi_k(x_h[i], k)
    y_met.append(cur_sum)
y_met.append(0)
e = [abs(y_met[i] - y_ex[i]) for i in range(len(y_met))]

print(f'{"Метод неопределенных коэффициентов": ^63}\n')
print_table(x_h, y_met, y_ex, e)
