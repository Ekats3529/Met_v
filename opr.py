

# создаем матрицу А
def generate_A(main_diag, n):
    return [[(main_diag[i] if j == i else main_diag[i] / 100) for j in range(n)] for i in range(n)]