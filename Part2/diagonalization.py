from Jacobi import jacobi_eigenvalue, transpose, matrix_multiply
def diagonalize_symmetric(A):
    """
    Chéo hóa ma trận đối xứng A và sắp xếp trị riêng giảm dần.
    Trả về ma trận P, D, và P_inv sao cho A = P * D * P_inv.
    """
    n = len(A)
    #Tìm trị riêng và vector riêng bằng Jacobi
    #eigenvalues là list các trị riêng
    eigenvalues, P_raw = jacobi_eigenvalue(A)

    #Ghép trị riêng với vector riêng tương ứng để sắp xếp
    #P_raw có các cột là vector riêng, nên ta lấy P_raw[i][j] theo cột j
    eig_pairs = []
    for j in range(n):
        val = eigenvalues[j]
        vec = [P_raw[i][j] for i in range(n)] #vector riêng tương ứng với trị riêng j
        eig_pairs.append((val, vec))

    #Sắp xếp trị riêng giảm dần
    eig_pairs.sort(key=lambda x: x[0], reverse=True)

    #Tạo lại ma trận D và P sau khi đã sắp xếp
    D = [[0.0 for _ in range(n)] for _ in range(n)]
    P = [[0.0 for _ in range(n)] for _ in range(n)]

    sorted_eigenvalues = []
    for j in range(n):
        val_j = eig_pairs[j][0]
        vec_j = eig_pairs[j][1]

        sorted_eigenvalues.append(val_j)
        D[j][j] = val_j
        for i in range(n):
            P[i][j] = vec_j[i]

    #Tìm P^(-1), vì A đối xứng, P là ma trận trực giao => P^(-1) = P^T
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
