from Part2.Jacobi import jacobi_eigenvalue, transpose, matrix_multiply
from  Part1.inverse import inverse
import numpy as np
'''
chạy lệnh python -m Part2.diagonalization để chạy chương trình
'''


def solve_for_eigenvector(A, lamda, repeat_index=0):
    """
    Giải hệ (A - lambda*I)v = 0 bằng khử Gauss.
    repeat_index: Dùng để chọn biến tự do khác nhau khi trị riêng bị lặp.
    """
    n = len(A)
    #Tạo ma trận (A - lambda*I)
    M = [[A[i][j] - (lamda if i == j else 0) for j in range(n)] for i in range(n)]
    for row in M: row.append(0.0)

    #Khử Gauss đưa về dạng bậc thang
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

    #Giải ngược tìm vector riêng
    res = [0.0] * n
    #Thay đổi vị trí biến tự do dựa trên repeat_index để đảm bảo các vector riêng độc lập
    free_var_pos = (n - 1 - repeat_index) % n
    res[free_var_pos] = 1.0

    for i in range(n - 1, -1, -1):
        if abs(M[i][i]) > 1e-12:
            s = sum(M[i][j] * res[j] for j in range(i + 1, n))
            res[i] = -s / M[i][i]

    #Chuẩn hóa vector
    norm = sum(x ** 2 for x in res) ** 0.5
    return [x / (norm if norm > 1e-12 else 1.0) for x in res]

def is_symmetric(A):
    """Kiểm tra ma trận có đối xứng không."""
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j] - A[j][i]) > 1e-9: return False
    return True

def diagonalize_matrix(A):
    """
    Hàm chéo hóa kết hợp Numpy (cho bậc cao) và hàm tự viết (cho bậc thấp).
    """
    n = len(A)
    eigenvalues = []
    P_cols = []

    #Tính trị riêng
    if n >= 5:
        #Trường hợp bậc >= 5: Dùng numpy để tránh định lý Abel
        raw_eigs = np.linalg.eigvals(A).tolist()
        eigenvalues = [val.real if abs(getattr(val, 'imag', 0)) < 1e-10 else val for val in raw_eigs]
    else:
        #Trường hợp bậc < 5: Sử dụng Jacobi
        if is_symmetric(A):
            eigenvalues, V_raw = jacobi_eigenvalue(A)

            D = [[0.0 for _ in range(n)] for _ in range(n)]
            for i in range(n): D[i][i] = eigenvalues[i]
            P_inv = transpose(V_raw)
            return V_raw, D, P_inv
        else:
            # Nếu không đối xứng và n < 5, tạm dùng numpy để lấy trị riêng chính xác
            raw_eigs = np.linalg.eigvals(A).tolist()
            eigenvalues = [val.real if abs(getattr(val, 'imag', 0)) < 1e-10 else val for val in raw_eigs]

    #Tự tìm vector riêng
    counts = {}
    for lam in eigenvalues:
        #Làm tròn để nhan diện trị riêng lặp
        lam_key = round(lam, 8) if isinstance(lam, float) else lam
        idx = counts.get(lam_key, 0)
        v = solve_for_eigenvector(A, lam, repeat_index=idx)
        P_cols.append(v)
        counts[lam_key] = idx + 1

    #Tạo ma trận P từ các cột vector riêng
    P = [[P_cols[j][i] for j in range(n)] for i in range(n)]

    #Tạo ma trận D
    D = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n): D[i][i] = eigenvalues[i]

    #Tính nghịch đảo P bằng inverse
    P_inv = inverse(P)
    if isinstance(P_inv, str):
        print(f"Lỗi: {P_inv}")
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

    '''A_sym = [
        [4, 1],
        [1, 3]
    ]'''

    A_sym = [
        [0, -1],
        [1, 0]
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
