from Part1.helper_function import augmented_matrix, change_row, plus_another_row
from Part1.back_substitution import back_substitution
import copy

def gaussian_eliminate(A: list, b: list):
    """Hàm chính: Giải hệ phương trình Ax = b"""
    
    EPS = 1e-10
    n = len(A)
    if n == 0: return [], [], 0
    m = len(A[0])
    m_total = m + 1

    # ta dùng list comprehension ghép A và b trực tiếp.
    ref_matrix = [A[i] + [b[i]] for i in range(n)]

    row, col, swap_count = 0, 0, 0

    while row < n and col < m: 
        maxVal = -1.0
        max_row = -1
        for i in range(row, n):
            val = abs(ref_matrix[i][col])
            if val > maxVal:
                maxVal = val
                max_row = i

        # Nếu phần tử lớn nhất vẫn < EPS, coi như cột đó toàn số 0
        if maxVal < EPS:
            col += 1
            continue

        if max_row != row:
            ref_matrix[row], ref_matrix[max_row] = ref_matrix[max_row], ref_matrix[row]
            swap_count += 1

        pivot = ref_matrix[row][col]
        for i in range(row + 1, n):
            if abs(ref_matrix[i][col]) > EPS:
                c_factor = ref_matrix[i][col] / pivot
                
                for j in range(col, m_total):
                    ref_matrix[i][j] -= c_factor * ref_matrix[row][j]

        row += 1
        col += 1

    U = [r[:m] for r in ref_matrix]
    c_vec = [r[m] for r in ref_matrix]

    result = back_substitution(U, c_vec)

    return ref_matrix, result, swap_count
