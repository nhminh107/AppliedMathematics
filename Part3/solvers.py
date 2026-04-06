import copy
from Part1.helper_function import augmented_matrix

"""NOTE: ĐỂ CHẠY HÀM NÀY. Vào terminal gõ python -m Part3.solvers"""
def DLU_Decomposition(A: list): 
    """A là một ma trận tăng cường, phân rã A thành D + L + U """
    D_matrix = copy.deepcopy(A) 
    L_matrix = copy.deepcopy(A)
    U_matrix = copy.deepcopy(A) 

    for i in range(len(D_matrix)): 
        for j in range(len(D_matrix[i])): 
            if i != j: 
                D_matrix[i][j] = 0 # Chỉ giữ lại đường chéo

            if i >= j : 
                U_matrix[i][j] = 0 # Giữ lại tam giác trên

            if i <= j : 
                L_matrix[i][j] = 0 #Giữ lại tam giác dưới 

    return D_matrix, U_matrix, L_matrix

def canStop(x_old: list, x_new: list) -> bool:
    epsilon = 1e-10
    # Dùng zip để lấy từng cặp (cũ, mới) rồi trừ cho nhau
    return all(abs(o - n) < epsilon for o, n in zip(x_old, x_new))

def isConvergence(A: list) -> bool:
    """Check xem cái ma trận này có hội tụ không (theo tiêu chuẩn chéo trội nghiêm ngặt)"""

    for i in range(len(A)):
        diagonal_element = abs(A[i][i])
    
        sum_others = 0
        for j in range(len(A[i])): 
            if i != j:
                sum_others += abs(A[i][j])
        
        if diagonal_element <= sum_others:
            return False 

    return True


def iteratorSolve(A:list, b:list) : 
    epsilon = 1e-10 
    if not isConvergence(A):
        return "Ma trận không chéo trội chặt hàng"
        
    augMatrix = augmented_matrix(A, b) 
    x_vector = [0]*len(b) #Đây là ma trận lưu x mới
    x_lass_vector = [0]*len(b) #Đây là ma trận lưu x cũ 
    D_matrix, U_matrix, L_matrix = DLU_Decomposition(augMatrix) #Chưa thấy cần dùng ở đâu
    n = len(A)  
    max_iter = 2000 
    for i in range(max_iter): 
        stopIt = False 
        # CẦN THIẾT: Lưu lại vector cũ trước khi bước vào tính toán vòng lặp mới
        x_lass_vector = x_vector.copy() 

        for ii in range(n): 
            #Zichma đầu tiên
            sum_first_zichma = 0 
            for j in range(0, ii): # Sửa: j chạy từ 0 đến ii-1
                sum_first_zichma += A[ii][j] * x_vector[j] # Sửa: A[ii][j]
            #Zichma thứ 2 
            sum_sec_zichma = 0 
            for j in range(ii+1, n): 
                sum_sec_zichma += A[ii][j] * x_lass_vector[j] # Sửa: A[ii][j]

            # Tính giá trị mới cho x_vector[ii]
            x_vector[ii] = b[ii] - sum_first_zichma - sum_sec_zichma
            x_vector[ii] /= A[ii][ii]

            if ii == n - 1: 
                stopIt = canStop(x_lass_vector, x_vector) 
        
        if stopIt:
            break 
    
    return x_vector

if __name__ == "__main__": 
    A = [[1,2,3], [4,5,6], [7,8,9], [10,11, 12]]
    D, U, L = DLU_Decomposition(A)

    print(D)
    print(U)
    print(L)

    A1 = [[10, 2], 
        [1, 5]]
    B1 = [12, 6]
    # Kết quả đúng: x = [1, 1]
    print(iteratorSolve(A1, B1))