import math
from Part2.Jacobi import transpose, matrix_multiply, jacobi_eigenvalue


def svd_decompose(A):
    m = len(A)
    n = len(A[0])

    A_T = transpose(A)
    M = matrix_multiply(A_T, A)

    eigenvalues, V = jacobi_eigenvalue(M, 1e-15, 500)

    eig_pairs = []
    for j in range(n):
        eig_val = eigenvalues[j] if eigenvalues[j] > 1e-10 else 0.0
        col = [V[i][j] for i in range(n)]
        eig_pairs.append((eig_val, col))

    eig_pairs.sort(key=lambda x: x[0], reverse=True)

    Sigma = [[0.0 for _ in range(n)] for _ in range(m)]
    V_sorted = [[0.0 for _ in range(n)] for _ in range(n)]
    singular_values = []

    for j in range(n):
        val = math.sqrt(eig_pairs[j][0])
        singular_values.append(val)
        if j < min(m, n):
            Sigma[j][j] = val
        for i in range(n):
            V_sorted[i][j] = eig_pairs[j][1][i]

    V_T = transpose(V_sorted)

    U = [[0.0 for _ in range(m)] for _ in range(m)]
    for j in range(min(m, n)):
        sigma = singular_values[j]
        if sigma > 1e-10:
            v_j = [V_sorted[i][j] for i in range(n)]
            Av = [sum(A[r][c] * v_j[c] for c in range(n)) for r in range(m)]
            for r in range(m):
                U[r][j] = Av[r] / sigma

            for k in range(j):
                dot = sum(U[r][k] * U[r][j] for r in range(m))
                for r in range(m):
                    U[r][j] -= dot * U[r][k]

            norm = math.sqrt(sum(U[r][j] ** 2 for r in range(m)))
            if norm > 1e-10:
                for r in range(m):
                    U[r][j] /= norm

    for j in range(m):
        col_norm = sum(U[r][j] ** 2 for r in range(m))
        if col_norm < 1e-10:
            for i in range(m):
                v = [1.0 if x == i else 0.0 for x in range(m)]
                for k in range(j):
                    dot = sum(U[r][k] * v[r] for r in range(m))
                    for r in range(m):
                        v[r] -= dot * U[r][k]
                norm = math.sqrt(sum(x ** 2 for x in v))
                if norm > 1e-10:
                    for r in range(m):
                        U[r][j] = v[r] / norm
                    break

    return U, Sigma, V_T