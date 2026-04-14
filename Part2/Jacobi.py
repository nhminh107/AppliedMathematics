import math

def transpose(matrix):
    """Tính ma trận chuyển vị - Tối ưu hóa bằng zip."""
    return [list(row) for row in zip(*matrix)]


def matrix_multiply(A, B):
    """Nhân hai ma trận A và B - Tối ưu hóa bằng zip và pre-transpose."""
    #Chuyển vị B để truy cập các cột như các hàng, giúp tăng tốc độ zip
    B_T = list(zip(*B))
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in B_T] for row_a in A]


def jacobi_eigenvalue(A, tol=1e-9, max_sweeps=50):
    """
    Thuật toán Cyclic Jacobi tối ưu:
    - Loại bỏ bước tìm max O(N^2).
    - Duyệt tuần tự qua các phần tử ngoài đường chéo.
    - Sử dụng các phép tính đại số thay cho hàm lượng giác tốn kém.
    """
    n = len(A)
    # Khởi tạo ma trận vector riêng V là ma trận đơn vị
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    # Tạo bản sao của A để tính toán
    A_copy = [row[:] for row in A]

    # Một 'sweep' là một lượt duyệt qua toàn bộ các phần tử ngoài đường chéo
    for sweep in range(max_sweeps):
        changed = False
        for p in range(n - 1):
            for q in range(p + 1, n):
                # Chỉ xử lý nếu phần tử ngoài đường chéo đủ lớn
                if abs(A_copy[p][q]) < tol:
                    continue

                changed = True

                # Tính toán các hệ số quay (c, s, tau) không dùng atan2/sin/cos
                app = A_copy[p][p]
                aqq = A_copy[q][q]
                apq = A_copy[p][q]

                diff = aqq - app
                if abs(apq) < tol * abs(diff):
                    t = apq / diff
                else:
                    phi = diff / (2.0 * apq)
                    t = 1.0 / (abs(phi) + math.sqrt(1.0 + phi ** 2))
                    if phi < 0: t = -t

                c = 1.0 / math.sqrt(1.0 + t ** 2)
                s = t * c
                tau = s / (1.0 + c)

                # Cập nhật A[p][p], A[q][q] và triệt tiêu A[p][q]
                A_copy[p][p] -= t * apq
                A_copy[q][q] += t * apq
                A_copy[p][q] = A_copy[q][p] = 0.0

                # Cập nhật các phần tử còn lại của ma trận A
                for i in range(n):
                    if i != p and i != q:
                        a_ip = A_copy[i][p]
                        a_iq = A_copy[i][q]
                        A_copy[i][p] = A_copy[p][i] = a_ip - s * (a_iq + tau * a_ip)
                        A_copy[i][q] = A_copy[q][i] = a_iq + s * (a_ip - tau * a_iq)

                    # Cập nhật ma trận vector riêng V
                    v_ip = V[i][p]
                    v_iq = V[i][q]
                    V[i][p] = v_ip - s * (v_iq + tau * v_ip)
                    V[i][q] = v_iq + s * (v_ip - tau * v_iq)

        # Nếu sau một lượt quét không có thay đổi nào đáng kể thì dừng sớm
        if not changed:
            break

    eigenvalues = [A_copy[i][i] for i in range(n)]
    return eigenvalues, V
