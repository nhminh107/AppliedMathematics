import copy
def augmented_matrix(A: list, b: list):
    """INPUT: Matrix A, b in Ax = b
       Output: A_augmented = (A|B)"""
    return [row + [val] for row, val in zip(A, b)]

def change_row(A: list, idx1 : int, idx2: int):
    """Truyền idx1, idx2 theo số bắt đầu từ 1 cho giống với làm bài bình thường, đỡ nhầm"""
    if idx1 > len(A) or idx2 > len(A):
        return -1
    temp = A[idx1]
    A[idx1] = A[idx2]
    A[idx2] = temp

def multiply_row_with_c(A: list, idx1 : int, c: int):
    """Nhân một dòng với số c"""
    if idx1> len(A):
        return -1

    for i in range(len(A[idx1])):
        A[idx1][i] *= c

def plus_another_row(A: list, idx1: int, idx2: int, c: int):
    """Input: Ma trận A, idx1 là hàng được cộng, c là số nhân
    R_idx1 <- R_idx1 + c*R_idx2"""
    A_copy = copy.deepcopy(A)
    multiply_row_with_c(A_copy, idx2, c)

    for i in range(len(A[idx1])):
        A[idx1][i] += A_copy[idx2][i]

def isREF(A: list):
    """Check xem đã phải ma trận bậc thang chưa"""
    prev_pivot = -1
    for i in range(len(A)):
        curr_pivot = -1
        for j in range(len(A[0])):
            if abs(A[i][j]) > 1e-10:
                curr_pivot = j
                break

        if curr_pivot == -1:
            prev_pivot = float('inf')
        else:
            if curr_pivot <= prev_pivot:
                return False
            prev_pivot = curr_pivot
    return True