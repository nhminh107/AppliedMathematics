import math
from Jacobi import transpose, matrix_multiply, jacobi_eigenvalue

def svd_decompose(A):
    """Phân rã SVD cho ma trận A."""
    m = len(A)
    n = len(A[0])

    # Tính A^T * A
    A_T = transpose(A)
    M = matrix_multiply(A_T, A)

    # Lấy giá trị riêng và vector riêng từ hàm Jacobi
    eigenvalues, V = jacobi_eigenvalue(M)

    # Ghép và sắp xếp giảm dần theo trị riêng
    eig_pairs = []
    for j in range(n):
        eig_val = eigenvalues[j] if eigenvalues[j] > 1e-10 else 0.0
        col = [V[i][j] for i in range(n)]
        eig_pairs.append((eig_val, col))
    
    eig_pairs.sort(key=lambda x: x[0], reverse=True)

    # Khởi tạo Sigma, V_sorted
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

    # Xây dựng U
    U = [[0.0 for _ in range(m)] for _ in range(m)]
    for j in range(min(m, n)):
        sigma = singular_values[j]
        if sigma > 1e-10:
            v_j = [V_sorted[i][j] for i in range(n)]
            Av = [sum(A[r][c] * v_j[c] for c in range(n)) for r in range(m)]
            for r in range(m):
                U[r][j] = Av[r] / sigma

    return U, Sigma, V_T

if __name__ == "__main__":
    # Test thử với một ma trận đơn giản
    A_test = [
        [3, 2, 2],
        [2, 3, -2]
    ]
    
    U, Sigma, V_T = svd_decompose(A_test)
    
    print("--- Ma trận U ---")
    for row in U: print([round(x, 4) for x in row])
        
    print("\n--- Ma trận Sigma ---")
    for row in Sigma: print([round(x, 4) for x in row])
        
    print("\n--- Ma trận V^T ---")
    for row in V_T: print([round(x, 4) for x in row])
