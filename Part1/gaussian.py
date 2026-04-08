from Part1.helper_function import augmented_matrix, change_row, plus_another_row
from Part1.back_substitution import back_substitution
import copy

def gaussian_eliminate(A: list, b: list):
    """Hàm chính: Giải hệ phương trình Ax = b"""

    augMatrix = augmented_matrix(A, b)

    ref_matrix = copy.deepcopy(augMatrix)
    n = len(ref_matrix)
    m_total = len(ref_matrix[0])

    row, col, swap_count = 0, 0, 0

    while row < n and col < m_total:
        maxVal = -1
        max_row = -1

        for i in range(row, n):
            if abs(ref_matrix[i][col]) > maxVal:
                maxVal = abs(ref_matrix[i][col])
                max_row = i

        if abs(ref_matrix[max_row][col]) < 1e-10:
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

    n, m = len(A), len(A[0])

    for i in range(n):
        is_zero_row_A = True
        for j in range(m):
            if abs(ref_matrix[i][j]) > 1e-10:
                is_zero_row_A = False
                break

        if is_zero_row_A and abs(ref_matrix[i][m]) > 1e-10:
            return ref_matrix, "Vô nghiệm", swap_count

    U = [row[:m] for row in ref_matrix]
    c_vec = [row[m] for row in ref_matrix]

    result = back_substitution(U, c_vec)

    return ref_matrix, result, swap_count