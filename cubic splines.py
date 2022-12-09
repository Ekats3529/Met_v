import numpy as np
import gauss

X = [0, 1, 2, 3]
Y = [5, 6, 9, 13]
h = 1
n = 3


def create_matrix():
    view_2 = [[1 if i * 4 == j else 0 for j in range(4 * n)] for i in range(0, n)]
    view_3 = [[1 if (i - 1) * 4 <= j < i * 4 else 0 for j in range(4 * n)] for i in range(1, n + 1)]

    view_6 = [[0, 1, 2, 3, 0, 1] + [0 for i in range(6)]] + \
             [[0 for i in range(4)] + [0, 1, 2, 3, 0, 1] + [0, 0]]

    view_7 = [[0, 0, 2, 6, 0, 0, 2, 0] + [0 for i in range(4)]] + \
             [[0 for i in range(4)] + [0, 0, 2, 6, 0, 0, 2, 0]]

    view_8 = [[0, 0, 2] + [0 for i in range(9)]]

    view_9 = [[0 for i in range(10)] + [2, 6]]

    b = [5, 6, 9, 6, 9, 13, 0, 0, 0, 0, 0, 0]
    A = view_2 + view_3 + view_6 + view_7 + view_8 + view_9

    return (A, b)


print("\nCubic splines\n")

print("X:", end=" ")
for x in X:
    print(f'{x: >5.2f}', end=" ")
print()
print("Y:", end=" ")
for y in X:
    print(f'{y: >5.2f}', end=" ")
print("\n")

A, b = create_matrix()

print("Матрица A:")
for row in A:
    for c in row:
        print(f'{c: >5.2f}', end=" ")
    print()
print()

print("Матрица b:")
for c in b:
    print(f'{c: >5.2f}')

print()

solution = gauss.method_Gauss(A, b)  # решаем систему Ax = b

print("Решение СЛАУ:")

for c in solution:
    print(f'{c: >10.5f}', end="")

print("\n")

print('Значения в узловых точках:')

x_new = [0.5, 1.5, 2.5]
for i in range(len(x_new)):
    h_i = x_new[i] - X[i]
    i_for_func = len(X) * i
    func = solution[len(X) * i] + solution[len(X) * i + 1] * h_i + solution[len(X) * i + 2] * h_i ** 2 + \
           solution[len(X) * i + 3] * h_i ** 3
    print(f'f({x_new[i]:.1f}) = {func:.3f}')

print()

