import gauss
import numpy as np


def inverse(A):
    result = []
    for i in range(0, n):
        b_k = [0 for _ in range(0, i)] + [1] + [0 for _ in range(i + 1, n)]
        result.append(gauss.method_Gauss(A, b_k))
    return result


def check(M1, M2):
    A = np.array(M1)
    B = np.array(M2)
    return np.multiply(A,B)


v = 7  # номер варианта
n = 5  # размерность матрицы

main_diag = gauss.make_main_diag(v, n)  # создаем список элементов главной диагонали
A = gauss.generate_A(main_diag, n)  # создаем матрицу А

print("Матрица A:")
for row in A:
    for c in row:
        print(f'{c: >5.2f}', end=" ")
    print()
print()

A_1 = inverse(A)
print("Матрица A_1:")
for row in A_1:
    for c in row:
        print(f'{c: >5.2f}', end=" ")
    print()
print()


E = check(A, A_1)

print("Check")
for row in E:
    for c in row:
        print(f'{c: >5.2f}', end=" ")
    print()