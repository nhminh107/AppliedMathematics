def inverse(A : list):
    n = len(A)
    if any([len(A[i]) != n for i in range(n)]):
        return "Ma tran khong vuong, khong co nghich dao!"
    
    # Tao ma tran don vi I
    I = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    # Tao ma tran [A | I]
    M = [row_A + row_I for row_A, row_I in zip(A, I)]

    # Gauss-Jordan
    for i in range(n):
        # Chon phan tu chot (Partial Pivoting)
        pivot_row = i
        for j in range(i + 1, n):
            if abs(M[j][i]) > abs(M[pivot_row][i]):
                pivot_row = j

        M[i], M[pivot_row] = M[pivot_row], M[i]

        # Kiem tra ma tran suy bien
        if abs(M[i][i]) < 1e-10:
            return "Ma tran suy bien, khong co nghich dao!"

        # Chuan hoa dong chua pivot ve 1
        pivot_val = M[i][i]
        M[i] = [x / pivot_val for x in M[i]]

        # Khu cac phan tu khac tren cung cot ve 0
        for j in range(n):
            if i != j:
                factor = M[j][i]
                M[j] = [val_j - factor * val_i for val_i, val_j in zip(M[i], M[j])]

    # Trich xuat phan ma tran ben phai [I | A_inv]
    A_inv = [row[n:] for row in M]
    return A_inv

# Testcase cho hàm inverse
A = [
    [4.0, 7.0],
    [2.0, 6.0]
]

result = inverse(A)

if isinstance(result, str):
    print(result)
else:
    print("Ma trận nghịch đảo của A:")
    for row in result:
        # Làm tròn đến 2 chữ số thập phân để dễ nhìn
        print([round(x, 2) for x in row])

# Kiểm tra lại: A * A_inv nên xấp xỉ ma trận đơn vị I