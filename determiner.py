import gauss
import numpy as np
from copy import deepcopy


def determinant(M):
    n = len(M)
    res = deepcopy(M)

    mas = []

    for i in range(n):
        elem = res[i][i]
        mas.append(elem)
        for j in range(n):
            res[i][j] /= elem
        for k in range(i + 1, n):
            elem = res[k][i]
            for j in range(n):
                res[k][j] -= res[i][j] * elem

    det = 1
    for i in range(len(mas)):
        det *= mas[i]

    print(f"Gauss: {det}")


def determiner_np(M):
    A = np.array(M, float)
    print(f"Numpy: {np.linalg.det(A)}")


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


determinant(A)
determiner_np(A)



