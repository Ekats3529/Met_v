X = [0, 1, 2, 3]
Y = [7, 8, 11, 15]


def y(x):
    return (-1. / 6) * (x * x * x) + 1.5 * (x * x) + (-1. / 3) * x + 7


k = 0.5
for i in range(3):
    print(k + i, y(k + i))

for i in range(4):
    print(i, y(i))