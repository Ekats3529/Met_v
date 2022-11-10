# метод Гаусса
def method_Gauss(A, b):
    n = len(A)
    # формируем матрицу, с которой будем работать
    res = []
    for i in range(n):
        cur_lst = [A[i][j] for j in range(n)]
        cur_lst.append(b[i])
        res.append(cur_lst)

    # прямой ход
    # внешний цикл по строкам, с которыми работаем
    for i in range(n):
        # запоминаем первый ненулевой элемент строки i
        elem = res[i][i]
        # делим текущую (i-ю) строку на её первый ненулевой элемент
        for j in range(i, n + 1):
            res[i][j] /= elem

        # цикл по оставшимся строкам матрицы
        for k in range(i + 1, n):
            # запоминаем первый ненулевой элемент строки k
            elem = res[k][i]
            # вычитаем из строки k i-ю, домноженную на первый ненулевой элемент строки k
            for j in range(i, n + 1):
                res[k][j] -= res[i][j] * elem

    # обратный ход
    x = []
    for i in range(n):
        # кладем в x_cur i-е значение столбца b
        x_cur = res[n - i - 1][n]
        # вычитаем произведения элементов матрицы A на посчитанные иксы
        for j in range(i):
            x_cur -= res[n - i - 1][n - j - 1] * x[j]
        x.append(x_cur)

    # переворачиваем список решений, так как при добавлении шли с конца
    x.reverse()
    return x


# создаем список элементов главной диагонали
def make_main_diag(v, n):
    return [v + i for i in range(n)]


# создаем матрицу А
def generate_A(main_diag, n):
    return [[(main_diag[i] if j == i else main_diag[i] / 100) for j in range(n)] for i in range(n)]


# создаем матрицу b
def count_b(A, main_diag):
    return [sum([A[i][j] * main_diag[j] for j in range(n)]) for i in range(n)]


def check(A, x):
    return [sum([A[i][j] * x[j] for j in range(n)]) for i in range(n)]


v = 7  # номер варианта
n = 5  # размерность матрицы

main_diag = make_main_diag(v, n)  # создаем список элементов главной диагонали
A = generate_A(main_diag, n)  # создаем матрицу А

print("Матрица A:")
for row in A:
    for c in row:
        print(f'{c: >5.2f}', end=" ")
    print()

b = count_b(A, main_diag)  # создаем матрицу b

print("Матрица b:")
for c in b:
    print(f'{c: >5.2f}')  # , end = " ")

x = method_Gauss(A, b)  # решаем систему Ax = b
print("Решение СЛАУ:")

for c in x:
    print(f'{c: >10.5f}', end="")

print()
print("Проверка: ")
new_b = check(A, x)

for c in new_b:
    print(f'{c: >5.2f}')
