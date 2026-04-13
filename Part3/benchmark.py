from Part1.gaussian import gaussian_eliminate
from Part2.decomposition import svd_decompose
from Part2.Jacobi import transpose, matrix_multiply, jacobi_eigenvalue 
from Part3.solvers import iteratorSolve 
import time 
import math 
import random
import matplotlib.pyplot as plt 


def gaussian_solve(A:list, b:list): 
    x = gaussian_eliminate(A, b)[1] 
    return [float(s.split('=')[1]) for s in x]

def svd_solve(A, b):
    """
    Giải hệ phương trình Ax = b bằng phương pháp SVD.
    Sử dụng hàm svd_decompose đã có.
    """
    U, Sigma, V_T = svd_decompose(A)
    
    m = len(U) 
    n = len(V_T) 
    
    U_T = transpose(U)
    d = [sum(U_T[i][j] * b[j] for j in range(m)) for i in range(m)]
    
    z = [0.0] * n
    for i in range(min(m, n)):
        sigma_i = Sigma[i][i]
        if sigma_i > 1e-10:
            z[i] = d[i] / sigma_i
        else:
            z[i] = 0.0
    V = transpose(V_T)
    x = [sum(V[i][j] * z[j] for j in range(n)) for i in range(n)]
    
    return x

import math

def norm_of_vector(x: list): 
    res = 0 
    for i in x: 
        res += i*i
    return math.sqrt(res) 

def relative_error(A: list, b: list, x: list): 
    if x == "Vô nghiệm": 
        return 0

    elif x[2] == "x_3 (ẩn tự do)": 
        return 0
    
    n = len(A)
    Ax_vector = []
    for i in range(n):
        row_sum = sum(A[i][j] * x[j] for j in range(len(x)))
        Ax_vector.append(row_sum)
    
    r = [i - j for (i, j) in zip(Ax_vector, b)] 
    
    norm_r = norm_of_vector(r) 
    norm_b = norm_of_vector(b) 
    
    if norm_b == 0: return norm_r
    return norm_r / norm_b

def benchmark_for_gaussian(LSTest: list): 
    """A là bộ test, bao gồm list các [A, b]""" 
    
    time_record = []
    relative_error_record = []
    
    for testcase in LSTest: 
        start_time = time.perf_counter()
        x = gaussian_solve(testcase[0], testcase[1]) 
        end_time = time.perf_counter() 
        time_record.append(end_time - start_time) 

        rela_err = relative_error(testcase[0], testcase[1], x) 
        relative_error_record.append(rela_err)
    
    return time_record, relative_error_record

def benchmark_for_svd_solver(LSTest: list): 
    """A là bộ test, bao gồm list các [A, b]""" 
    
    time_record = []
    relative_error_record = []
    
    for testcase in LSTest: 
        start_time = time.perf_counter()
        x = svd_solve(testcase[0], testcase[1]) 
        end_time = time.perf_counter() 
        time_record.append(end_time - start_time) 

        rela_err = relative_error(testcase[0], testcase[1], x) 
        relative_error_record.append(rela_err)
    
    return time_record, relative_error_record

def benchmark_for_iterator_solver(LSTest: list): 
    """A là bộ test, bao gồm list các [A, b]""" 
    
    time_record = []
    relative_error_record = []
    
    for testcase in LSTest: 
        start_time = time.perf_counter()
        x = iteratorSolve(testcase[0], testcase[1]) 
        end_time = time.perf_counter() 
        time_record.append(end_time - start_time) 

        rela_err = relative_error(testcase[0], testcase[1], x) 
        relative_error_record.append(rela_err)
    
    return time_record, relative_error_record

def benchmark(): 
    sizes = [50, 100, 200, 500, 1000] 
    
    # 1. Khởi tạo dictionary để lưu thời gian
    time_records = {
        "Gaussian": [],
        "SVD": [],
        "Iterative": []
    }
    
    print(f"{'N':<6} | {'Method':<15} | {'Time (ms)':<12} | {'Relative Error':<15}")
    print("-" * 55)

    for n in sizes: 
        test_data = []
        for _ in range(5):
            A = [[random.uniform(1, 10) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                row_sum = sum(abs(A[i][j]) for j in range(n) if i != j)
                A[i][i] = row_sum + random.uniform(1, 5)
                
            b = [random.uniform(-100, 100) for _ in range(n)]
            test_data.append([A, b]) 

        methods = [
            ("Gaussian", benchmark_for_gaussian),
            ("SVD", benchmark_for_svd_solver),
            ("Iterative", benchmark_for_iterator_solver)
        ]

        for name, func in methods:
            try:
                times, errors = func(test_data)
                avg_time = (sum(times) / len(times)) * 1000 
                avg_error = sum(errors) / len(errors)

                time_records[name].append(avg_time)
                
                print(f"{n:<6} | {name:<15} | {avg_time:>10.2f} | {avg_error:>15.2e}")
            except Exception as e:
                time_records[name].append(None) 
                print(f"{n:<6} | {name:<15} | {'Error':>10} | {str(e)[:15]}")
        print("-" * 55)
    
    print("Đồ thị LOG-LOG")
    plot_log_log(sizes, time_records)
    
    
def plot_log_log(sizes, time_records):
    plt.figure(figsize=(10, 6))
    
    for method, times in time_records.items():
        valid_sizes = [s for s, t in zip(sizes, times) if t is not None]
        valid_times = [t for t in times if t is not None]
        
        if valid_times:
            marker = 'o' if method == 'Gaussian' else 's' if method == 'SVD' else '^'
            plt.plot(valid_sizes, valid_times, marker=marker, label=method)
    
    valid_gauss_times = [t for t in time_records['Gaussian'] if t is not None]
    if valid_gauss_times:
        c = valid_gauss_times[0] / (sizes[0]**3)
        theoretical_O3 = [c * (n**3) for n in sizes]
        plt.plot(sizes, theoretical_O3, 'k--', label='$O(n^3)$ Theoretical')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Kích thước ma trận n (log scale)')
    plt.ylabel('Thời gian chạy (ms) (log scale)')
    plt.title('Log-Log Plot: Thời gian chạy vs Kích thước n')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

def generate_hilbert_matrix(n):
    """Tạo ma trận Hilbert (Ill-conditioned)"""
    return [[1.0 / (i + j + 1) for j in range(n)] for i in range(n)]

def generate_spd_matrix(n):
    """Tạo ma trận Random SPD (Well-conditioned)"""
    A = [[random.uniform(-1, 1) for _ in range(n)] for _ in range(n)]
    A_T = transpose(A)
    # Nhân A * A^T để ma trận mang tính đối xứng dương (SPD)
    A_spd = [[sum(A[i][k] * A_T[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    
    # Cộng thêm n vào đường chéo để đảm bảo chéo trội / SPD mạnh
    for i in range(n):
        A_spd[i][i] += n 
    return A_spd

def analyze_stability():
    sizes = [10, 20, 50] # Test ở các kích thước nhỏ và vừa vì Hilbert sai số rất nhanh
    print("\n" + "="*60)
    print(" BẮT ĐẦU PHÂN TÍCH TÍNH ỔN ĐỊNH (HILBERT vs SPD)")
    print("="*60)
    
    for n in sizes:
        print(f"\n--- Kích thước N = {n} ---")
        
        # Giả sử vector nghiệm đúng x = [1, 1, ..., 1]
        x_true = [1.0] * n
        
        # 1. Tạo Testcase với ma trận Hilbert
        H = generate_hilbert_matrix(n)
        b_H = [sum(H[i][j] * x_true[j] for j in range(n)) for i in range(n)]
        
        # 2. Tạo Testcase với ma trận SPD
        S = generate_spd_matrix(n)
        b_S = [sum(S[i][j] * x_true[j] for j in range(n)) for i in range(n)]
        
        methods = [
            ("Gaussian", gaussian_solve),
            ("SVD", svd_solve)
        ]
        
        print(f"{'Phương pháp':<15} | {'Sai số Hilbert (Ill)':<20} | {'Sai số SPD (Well)':<20}")
        print("-" * 60)
        
        for name, solver in methods:
            # Test ma trận Hilbert
            try:
                x_H = solver(H, b_H)
                err_H = relative_error(H, b_H, x_H)
            except:
                err_H = float('inf')
                
            # Test ma trận SPD
            try:
                x_S = solver(S, b_S)
                err_S = relative_error(S, b_S, x_S)
            except:
                err_S = float('inf')
                
            print(f"{name:<15} | {err_H:<20.2e} | {err_S:<20.2e}")

analyze_stability()
benchmark()