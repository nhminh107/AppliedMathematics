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

def multipli_row_with_c(A: list, idx1 : int, c: int): 
    """Nhân một dòng với số c""" 
    if idx1> len(A): 
        return -1
    
    for i in range(len(A[idx1])):  
        A[idx1][i] *= c 
    
def plus_another_row(A: list, idx1: int, idx2: int, c: int): 
    """Input: Ma trận A, idx1 là hàng được cộng, c là số nhân
    R_idx1 <- R_idx1 + c*R_idx2"""
    A_copy = copy.deepcopy(A) 
    multipli_row_with_c(A_copy, idx2, c) 

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
    augMatrix = copy.deepcopy([row + [val] for row, val in zip(A, b)])
    n = len(A)
    m = len(A[0])
    swap_count = 0

    for i in range(min(n, m)):
        max_row = i
        for k in range(i + 1, n):
            if abs(augMatrix[k][i]) > abs(augMatrix[max_row][i]):
                max_row = k
        
        if abs(augMatrix[max_row][i]) < 1e-10:
            continue
            
        if max_row != i:
            augMatrix[i], augMatrix[max_row] = augMatrix[max_row], augMatrix[i]
            swap_count += 1
            
        for k in range(i + 1, n):
            factor = augMatrix[k][i] / augMatrix[i][i]
            for j in range(i, m + 1):
                augMatrix[k][j] -= factor * augMatrix[i][j]

    x = [0.0] * m
    has_unique = (n >= m)
    
    if has_unique:
        for i in range(m):
            if abs(augMatrix[i][i]) < 1e-10:
                has_unique = False
                break

    if has_unique:
        for i in range(m - 1, -1, -1):
            s = sum(augMatrix[i][j] * x[j] for j in range(i + 1, m))
            x[i] = (augMatrix[i][m] - s) / augMatrix[i][i]
    else:
        x = None 

    return augMatrix, x, swap_count


#Đoạn dưới để test 

A = [[1,2,3], [4,5,6], [7, 8, 9]]
b = [1,2,3]
plus_another_row(A, 0, 1, 1) 
print(A)
print(augmented_matrix(A,b)) 