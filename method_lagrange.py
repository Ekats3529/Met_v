X = [0, 1, 2, 3]
Y = [7, 8, 11, 15]


def L(x, n):
    ans = 0
    for i in range(n + 1):
        res = 1
        for j in range(n + 1):
            if i != j:
                res *= (x - X[j]) / (X[i] - X[j])
        ans += res*Y[i]
    return ans


print("\nLagrange method\n")

k = 0.5
for i in range(3):
    print(f"f({k + i}): {L(k + i, 3)}")

print()

for i in range(4):
    print(f"f({i}): {L(i, 3)}")