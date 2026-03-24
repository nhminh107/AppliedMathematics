def inverse(A : list):
    n = len(A)
    # Tạo ma trận đơn vị I
    I = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    # Tạo ma trận [A | I]
    M = [row_A + row_I for row_A, row_I in zip(A, I)]

    # Gauss-Jordan
    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(M[j][i]) > abs(M[pivot_row][i]):
                pivot_row = j

        M[i], M[pivot_row] = M[pivot_row], M[i]

        if abs(M[i][i]) < 1e-10:
            return "Ma trận suy biến, không có nghịch đảo!"

        pivot_val = M[i][i]
        M[i] = [x / pivot_val for x in M[i]]

        for j in range(n):
            if i != j:
                factor = M[j][i]
                M[j] = [val_j - factor * val_i for val_i, val_j in zip(M[i], M[j])]

    A_inv = [row[n:] for row in M]
    return A_inv

# Đoạn test:
A = [[2, 1, 1], [4, -6, 0], [-2, 7, 2]]
print(inverse(A))