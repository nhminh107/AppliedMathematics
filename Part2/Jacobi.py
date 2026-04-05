import math

def transpose(matrix):
    """Tính ma trận chuyển vị."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(A, B):
    """Nhân hai ma trận A và B."""
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    result = [[0.0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def jacobi_eigenvalue(A, tol=1e-9, max_iter=100):
    """
    Thuật toán Jacobi tìm giá trị riêng và vector riêng cho ma trận đối xứng.
    """
    n = len(A)
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    A_copy = [[A[i][j] for j in range(n)] for i in range(n)]

    for _ in range(max_iter):
        max_val = 0.0
        p, q = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A_copy[i][j]) > max_val:
                    max_val = abs(A_copy[i][j])
                    p, q = i, j

        if max_val < tol:
            break

        # Xử lý trường hợp đặc biệt chia cho 0
        if A_copy[p][p] == A_copy[q][q]:
            theta = math.pi / 4 if A_copy[p][q] > 0 else -math.pi / 4
        else:
            theta = 0.5 * math.atan2(2 * A_copy[p][q], A_copy[p][p] - A_copy[q][q])

        c = math.cos(theta)
        s = math.sin(theta)

        A_pp = A_copy[p][p]
        A_qq = A_copy[q][q]
        A_pq = A_copy[p][q]

        A_copy[p][p] = c**2 * A_pp + 2*s*c*A_pq + s**2 * A_qq
        A_copy[q][q] = s**2 * A_pp - 2*s*c*A_pq + c**2 * A_qq
        A_copy[p][q] = A_copy[q][p] = 0.0

        for i in range(n):
            if i != p and i != q:
                A_ip = A_copy[i][p]
                A_iq = A_copy[i][q]
                A_copy[i][p] = A_copy[p][i] = c * A_ip + s * A_iq
                A_copy[i][q] = A_copy[q][i] = -s * A_ip + c * A_iq

            v_ip = V[i][p]
            v_iq = V[i][q]
            V[i][p] = c * v_ip + s * v_iq
            V[i][q] = -s * v_ip + c * v_iq

    eigenvalues = [A_copy[i][i] for i in range(n)]
    return eigenvalues, V
