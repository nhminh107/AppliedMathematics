from Part2.Jacobi import jacobi_eigenvalue, transpose, matrix_multiply
from  Part1.inverse import inverse
import numpy as np
'''
chạy lệnh python -m Part2.diagonalization để chạy chương trình
'''


def solve_for_eigenvector(A, lamda, index_for_repetition=0):
    """
    Giải hệ (A - lambda*I)v = 0.
    index_for_repetition: dùng để thay đổi vị trí biến tự do khi trị riêng lặp.
    """
    n = len(A)
    M = [[A[i][j] - (lamda if i == j else 0) for j in range(n)] for i in range(n)]
    for row in M: row.append(0.0)

    # Khử Gauss
    for i in range(n - 1):
        pivot = i
        for k in range(i + 1, n):
            if abs(M[k][i]) > abs(M[pivot][i]): pivot = k
        M[i], M[pivot] = M[pivot], M[i]
        if abs(M[i][i]) < 1e-12: continue
        for k in range(i + 1, n):
            factor = M[k][i] / M[i][i]
            for j in range(i, n + 1):
                M[k][j] -= factor * M[i][j]

    res = [0.0] * n
    #Thay đổi vị trí gán 1.0 dựa trên index_for_repetition để tránh vector trùng lặp
    target_idx = (n - 1 - index_for_repetition) % n
    res[target_idx] = 1.0

    for i in range(n - 1, -1, -1):
        if abs(M[i][i]) > 1e-12:
            s = sum(M[i][j] * res[j] for j in range(i + 1, n))
            res[i] = -s / M[i][i]

    norm = sum(x ** 2 for x in res) ** 0.5
    return [x / (norm if norm > 1e-12 else 1) for x in res]

def is_symmetric(A):
    """Kiểm tra ma trận có đối xứng không."""
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j] - A[j][i]) > 1e-9: return False
    return True

def diagonalize_matrix(A):
    """Hàm chéo hóa ma trận"""
    n = len(A)
    try:
        #Dùng np.linalg.eigvals cho trị riêng
        raw_eigenvalues = np.linalg.eigvals(A).tolist()
        eigenvalues = [val.real if abs(val.imag) < 1e-10 else val for val in raw_eigenvalues]
    except Exception as e:
        print(f"Lỗi trị riêng: {e}")
        return None, None, None  #Trả về 3 cái None để tránh lỗi unpack

    #Tự tìm vector riêng
    P_cols = []
    #Đếm số lần xuất hiện của từng trị riêng để xử lý lặp
    counts = {}
    for lam in eigenvalues:
        idx = counts.get(lam, 0)
        v = solve_for_eigenvector(A, lam, index_for_repetition=idx)
        P_cols.append(v)
        counts[lam] = idx + 1

    P = [[P_cols[j][i] for j in range(n)] for i in range(n)]

    #Tạo ma trận D
    D = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n): D[i][i] = eigenvalues[i]

    #Tự nghịch đảo
    P_inv = inverse(P)

    if isinstance(P_inv, str):
        print(f"Kết quả từ hàm inverse: {P_inv}")
        return None, None, None

    return P, D, P_inv

def verify_diagonalization(P, D, P_inv):
    """
    Nhân P * D * P^(-1) để kiểm tra xem có ra lại ma trận A không.
    """
    # Tính P * D
    PD = matrix_multiply(P, D)
    # Tính (P * D) * P_inv
    A_reconstructed = matrix_multiply(PD, P_inv)
    return A_reconstructed

if __name__ == "__main__":
    # Test chéo hóa với ma trận đối xứng

    A_sym = [
        [4, 1],
        [1, 3]
    ]


    print("--- Ma trận A ban đầu ---")
    for row in A_sym: print(row)

    # Thực hiện chéo hóa
    P, D, P_inv = diagonalize_matrix(A_sym)
    
    print("\n--- Ma trận P (Eigenvectors) ---")
    for row in P: print([round(x, 4) for x in row])

    print("\n--- Ma trận D (Eigenvalues) ---")
    for row in D: print([round(x, 4) for x in row])
        
    print("\n--- Ma trận P^(-1) ---")
    for row in P_inv: print([round(x, 4) for x in row])

    # Kiểm chứng: ráp lại công thức A = P * D * P^(-1)
    A_check = verify_diagonalization(P, D, P_inv)
    
    print("\n--- Kiểm chứng: P * D * P^(-1) ---")
    for row in A_check: print([round(x, 4) for x in row])
    # Kết quả in ra phải xấp xỉ [4, 1] và [1, 3]
