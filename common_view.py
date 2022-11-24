X = [0, 1, 2, 3]
Y = [7, 8, 11, 15]


def y(x):
    return (-1. / 6) * (x * x * x) + 1.5 * (x * x) + (-1. / 3) * x + 7


print("\nCommon view\n")

k = 0.5
for i in range(3):
    print(f"f({k + i}): {y(k + i)}")

print()

for i in range(4):
    print(f"f({i}): {y(i)}")