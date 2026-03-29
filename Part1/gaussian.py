import copy 
import getREF
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

def gaussian_eliminate(A: list, b: list):
    """Hàm chính: Giải hệ phương trình Ax = b"""
    augMatrix = augmented_matrix(A, b)
    ref_matrix, swap_count = get_REF(augMatrix)
    
    n, m = len(A), len(A[0])
    
    rank_a = 0
    for i in range(n):
        is_zero_row_A = True
        for j in range(m):
            if abs(ref_matrix[i][j]) > 1e-10:
                is_zero_row_A = False
                break
        
        if is_zero_row_A:
            if abs(ref_matrix[i][m]) > 1e-10:
                return ref_matrix, "Vô nghiệm", swap_count
        else:
            rank_a += 1

    if rank_a < m:
        return ref_matrix, "Vô số nghiệm", swap_count
    
    U = [r[:m] for r in ref_matrix]
    c = [r[m] for r in ref_matrix]
    x = [0.0] * m 
    for i in range(m - 1, -1, -1): 
        s = sum(U[i][j] * x[j] for j in range(i + 1, m))
        x[i] = (c[i] - s) / U[i][i]

    return ref_matrix, x, swap_count



"""A_1 = [[2, 1], [1, 3]]
b_1 = [0, 0]

print(gaussian_eliminate(A_1, b_1))"""
