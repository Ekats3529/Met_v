X = [0, 1, 2, 3]
Y = [7, 8, 11, 15]


def f(i, j):
    #print(i, j)
    if (j - i == 1):
        return (Y[j] - Y[i])/(X[j] - X[i])
    return (f(i + 1, j) - f(i, j - 1)) / (X[j] - X[i])


def N(x, n):
    ans = Y[0]
    for i in range(1, n+1):
        res = f(0, i)
        for j in range(0, i):
            res *= x - X[j]
        ans += res
    return ans



k = 0.5
for i in range(3):
    print(k + i, N(k + i, 3))

for i in range(4):
    print(i, N(i, 3))