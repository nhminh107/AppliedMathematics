import numpy as np
from Part2.Jacobi import jacobi_eigenvalue, transpose, matrix_multiply
from Part1.inverse import inverse
'''
python -m Part2.diagonalization
'''

def is_symmetric(A):
    """Kiểm tra ma trận đối xứng."""
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j] - A[j][i]) > 1e-9: return False
    return True


def solve_for_eigenvector(A, lamda, repeat_index=0):
    """Giải hệ (A - lambda*I)v = 0"""
    n = len(A)
    dtype = type(lamda)
    M = [[dtype(A[i][j]) - (lamda if i == j else dtype(0)) for j in range(n)] for i in range(n)]
    for row in M: row.append(dtype(0))

    for i in range(n - 1):
        pivot = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[pivot][i]): pivot = k
        M[i], M[pivot] = M[pivot], M[i]

        if abs(M[i][i]) < 1e-15: continue
        for k in range(i + 1, n):
            factor = M[k][i] / M[i][i]
            for j in range(i, n + 1):
                M[k][j] -= factor * M[i][j]

    res = [dtype(0)] * n
    free_var_pos = (n - 1 - repeat_index) % n
    res[free_var_pos] = dtype(1)

    for i in range(n - 1, -1, -1):
        if abs(M[i][i]) > 1e-15:
            s = sum(M[i][j] * res[j] for j in range(i + 1, n))
            res[i] = -s / M[i][i]

    norm = sum(abs(x) ** 2 for x in res) ** 0.5
    return [x / (norm if norm > 1e-15 else 1.0) for x in res]


def diagonalize_matrix(A):
    """
    Hàm chéo hóa ma trận
    """
    n = len(A)

    # Tìm Trị riêng
    if n >= 5:
        eigenvalues = np.linalg.eigvals(A).tolist()
    else:
        if is_symmetric(A):
            eigenvalues, V_raw = jacobi_eigenvalue(A)
            D = [[(eigenvalues[i] if i == j else 0.0) for j in range(n)] for i in range(n)]
            #Để ma trận luôn có trị riêng số thực
            return V_raw, D, transpose(V_raw)
        else:
            eigenvalues = np.linalg.eigvals(A).tolist()

    # Tìm Vector riêng
    P_cols = []
    counts = {}
    for lam in eigenvalues:
        lam_key = complex(round(lam.real, 10), round(lam.imag, 10)) if isinstance(lam, complex) else round(lam, 10)
        idx = counts.get(lam_key, 0)
        v = solve_for_eigenvector(A, lam, repeat_index=idx)
        P_cols.append(v)
        counts[lam_key] = idx + 1

    # Xây dựng P và D
    P = [[P_cols[j][i] for j in range(n)] for i in range(n)]
    D = [[(eigenvalues[i] if i == j else 0.0) for j in range(n)] for i in range(n)]

    # Tính P^-1
    P_inv = inverse(P)

    if isinstance(P_inv, str):
        return None, None, None

    # ép số thực nếu phần ảo cực nhỏ
    def smart_real(matrix):
        # Kiểm tra xem toàn bộ ma trận có phải gần như thực không
        is_effectively_real = all(all(abs(getattr(val, 'imag', 0)) < 1e-10 for val in row) for row in matrix)
        if is_effectively_real:
            return [[val.real if hasattr(val, 'real') else val for val in row] for row in matrix]
        return matrix

    return smart_real(P), smart_real(D), smart_real(P_inv)


def verify_diagonalization(P, D, P_inv):
    """Kiểm chứng bằng cách nhân lại ma trận."""
    PD = matrix_multiply(P, D)
    A_rec = matrix_multiply(PD, P_inv)
    return [[val.real if hasattr(val, 'real') else val for val in row] for row in A_rec]

if __name__ == "__main__":
    DiagonalTestCase = [
        [[4, 1], [1, 3]],
        [[2, -1, 0], [-1, 2, -1], [0, -1, 2]],
        [[5, 0], [0, -3]],
        [[0, -1], [1, 0]]
    ]

    def format_val(x):
        return round(x, 4)

    for i, A_test in enumerate(DiagonalTestCase):
        print(f"\n--- Testcase {i} ---")
        P, D, P_inv = diagonalize_matrix(A_test)
        if P:
            A_check = verify_diagonalization(P, D, P_inv)
            print("P * D * P^(-1):")
            for row in A_check: print([format_val(x) for x in row])