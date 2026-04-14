import math
from Part2.Jacobi import transpose, matrix_multiply, jacobi_eigenvalue


def svd_decompose(A):
    """Phân rã SVD cho ma trận A"""
    m = len(A)
    n = len(A[0])

    #Tính A^T * A
    A_T = transpose(A)
    M = matrix_multiply(A_T, A)

    #Chéo hóa M bằng Jacobi
    eigenvalues, V = jacobi_eigenvalue(M)

    #Sắp xếp trị riêng và vector riêng - Tối ưu bằng List Comprehension
    eig_pairs = sorted(
        [(v if v > 1e-10 else 0.0, [V[i][j] for i in range(n)]) for j, v in enumerate(eigenvalues)],
        key=lambda x: x[0], reverse=True
    )

    #Khởi tạo ma trận Sigma và V_sorted
    Sigma = [[0.0 for _ in range(n)] for _ in range(m)]
    V_sorted = [[0.0 for _ in range(n)] for _ in range(n)]
    singular_values = []

    for j in range(n):
        val = math.sqrt(eig_pairs[j][0])
        singular_values.append(val)
        if j < min(m, n):
            Sigma[j][j] = val
        #Gán vector riêng đã sắp xếp vào cột
        v_vec = eig_pairs[j][1]
        for i in range(n):
            V_sorted[i][j] = v_vec[i]

    V_T = transpose(V_sorted)

    #Xây dựng ma trận U - Tối ưu bằng cách nhân ma trận A * V
    #Thay vì tính từng Av cho mỗi cột, ta tính cả ma trận AV một lần
    AV = matrix_multiply(A, V_sorted)
    U = [[0.0 for _ in range(m)] for _ in range(m)]

    limit = min(m, n)
    for j in range(limit):
        sigma = singular_values[j]
        if sigma > 1e-10:
            for r in range(m):
                U[r][j] = AV[r][j] / sigma

    return U, Sigma, V_T