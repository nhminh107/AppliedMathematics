from Jacobi import jacobi_eigenvalue, transpose, matrix_multiply
def diagonalize_symmetric(A):
    """
    Chéo hóa ma trận đối xứng A.
    Trả về ma trận P, D, và P_inv sao cho A = P * D * P_inv.
    """
    n = len(A)
    
    # 1. Tìm giá trị riêng và vector riêng
    eigenvalues, P = jacobi_eigenvalue(A)
    
    D = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        D[i][i] = eigenvalues[i]
        
    # 2. Tìm P^(-1)
    # Vì A đối xứng, P là ma trận trực giao, nên P^(-1) = P^T
    P_inv = transpose(P)
    
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
    P, D, P_inv = diagonalize_symmetric(A_sym)
    
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
