def get_REF(M: list):
    """Hàm phụ trợ: Đưa ma trận M bất kỳ về dạng bậc thang (REF)"""
    ref_matrix = copy.deepcopy(M)
    n = len(ref_matrix)
    m = len(ref_matrix[0])
    row, col, swap_count = 0, 0, 0

    while row < n and col < m:
        maxVal = -1
        max_row = -1
        for i in range(row, n):
            if abs(ref_matrix[i][col]) > maxVal:
                maxVal = abs(ref_matrix[i][col])
                max_row = i

        if abs(ref_matrix[max_row][col]) < 1e-10:
            print(f"Không có pivot tại cột {col}")
            col += 1
            continue

        if max_row != row:
            change_row(ref_matrix, row, max_row)
            swap_count += 1

        for i in range(row + 1, n):
            c_factor = -ref_matrix[i][col] / ref_matrix[row][col]
            plus_another_row(ref_matrix, i, row, c_factor)

        row += 1
        col += 1

    return ref_matrix, swap_count
