import gauss


def run_through(A, d):
    n = len(A)
    a = [0] + [A[i][i - 1] for i in range(1, n - 1)] + [A[n - 1][n - 2]]
    b = [-A[i][i] for i in range(0, n - 1)] + [-A[n - 1][n - 1]]
    c = [A[i][i + 1] for i in range(0, n - 1)] + [0]

    p = [c[0] / b[0]]
    q = [-d[0] / b[0]]

    for i in range(n - 1):
        p.append(c[i + 1] / (b[i + 1] - a[i + 1] * p[i]))
        q.append((a[i + 1] * q[i] - d[i + 1]) / (b[i + 1] - a[i + 1] * p[i]))

    x = [0 for _ in range(n)]
    x[n - 1] = q[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = p[i - 1] * x[i] + q[i - 1]

    return x


def generate_A_for_run(main_diag, n):
    A = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if i == j:
                tmp.append(main_diag[i])
            elif i == j - 1 or i == j + 1:
                tmp.append(main_diag[i] / 100)
            else:
                tmp.append(0)
        A.append(tmp)
    return A


def count_d(A, list_for_variant):
    return [sum([A[i][j] * list_for_variant[j] for j in range(n)]) for i in range(n)]


v = 7  # номер варианта
n = 5  # размерность матрицы

main_diag = gauss.make_main_diag(v, n)  # создаем список элементов главной диагонали
A = generate_A_for_run(main_diag, n)  # создаем матрицу А

print("Матрица A:")
for row in A:
    for c in row:
        print(f'{c: >5.2f}', end=" ")
    print()
print()

d = count_d(A, main_diag)
print("Матрица d имеет вид:")
for c in d:
    print(f'{c: >5.2f}')

x = run_through(A, d)  # решаем систему Ax = b

print("Решение СЛАУ методом прогонки:")
for c in x:
    print(f'{c: >10.5f}', end="")
print()

print("Точное решение СЛАУ (методом Гаусса):")
for c in gauss.method_Gauss(A, d):
    print(f'{c: >10.5f}', end="")
