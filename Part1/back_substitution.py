def back_substitution(U: list, c: list):
    m = len(U[0])
    x = [0.0] * m
    for i in range(m - 1, -1, -1):
        s = sum(U[i][j] * x[j] for j in range(i + 1, m))
        x[i] = (c[i] - s) / U[i][i]
    return x
