from gaussian import gaussian_eliminate

def determinant(A):
    n = len(A)
    dummy_b = [0] * n 

    M, _, s = gaussian_eliminate(A, dummy_b)
    
    det = (-1) ** s
    for i in range(n):
        det *= M[i][i]
        
    return det

