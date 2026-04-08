from Part1.gaussian import gaussian_eliminate
from Part2.decomposition import svd_decompose
from Part2.Jacobi import transpose, matrix_multiply, jacobi_eigenvalue 
from Part3.solvers import iteratorSolve 
import time 
import math 
import random


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
    # 1. Thêm kích thước 1000 vào bộ test
    sizes = [50, 100, 200, 500, 1000] 
    
    print(f"{'N':<6} | {'Method':<15} | {'Time (ms)':<12} | {'Relative Error':<15}")
    print("-" * 55)

    for n in sizes: 
        test_data = []
        
        # 2. Lặp 5 lần để tạo 5 testcase ngẫu nhiên cho mỗi kích thước n
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
                
                # 3. Tính giá trị trung bình của 5 lần chạy
                avg_time = (sum(times) / len(times)) * 1000 
                avg_error = sum(errors) / len(errors)
                
                print(f"{n:<6} | {name:<15} | {avg_time:>10.2f} | {avg_error:>15.2e}")
            except Exception as e:
                print(f"{n:<6} | {name:<15} | {'Error':>10} | {str(e)[:15]}")
        print("-" * 55)
    
    
benchmark()