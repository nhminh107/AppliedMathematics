def back_substitution(U: list, c: list):
    m = len(U)
    if m == 0: return []
    n = len(U[0]) # Kích thước m x n
    
    # x[i] lưu biểu thức của x_i
    x = [[0.0] * (n + 1) for _ in range(n)]
    
    # Giả định ban đầu mọi biến đều là "ẩn tự do" (ví dụ: x2 = 1*x2)
    for i in range(n):
        x[i][i + 1] = 1.0 
        
    # Chạy ngược từ dòng cuối lên trên
    for i in range(m - 1, -1, -1):
        # Tìm phần tử (pivot) của dòng i
        p = -1
        for j in range(n):
            if abs(U[i][j]) > 1e-10:
                p = j
                break
                
        # Xử lý trường hợp dòng toàn số 0 (không có pivot)
        if p == -1:
            if abs(c[i]) > 1e-10:
                return "Hệ vô nghiệm"
            continue 
            
        # Rút biến cơ sở x_p theo các biến đằng sau nó
        x[p] = [0.0] * (n + 1)
        x[p][0] = c[i] / U[i][p]
        
        # Thế biểu thức của các x_j vào
        for j in range(p + 1, n):
            if abs(U[i][j]) > 1e-10:
                factor = -U[i][j] / U[i][p]
                # Cộng dồn hệ số: x_p = x_p + factor * x_j
                for k in range(n + 1):
                    x[p][k] += factor * x[j][k]
                    
    # Chuyển đổi mảng hệ số thành chuỗi công thức tổng quát
    ket_qua = []
    for i in range(n):
        tmp = x[i]
        
        # Nếu biểu thức chỉ có đúng 1*xi, nó là ẩn tự do
        if tmp[i + 1] == 1.0 and all(abs(tmp[k]) < 1e-10 for k in range(n + 1) if k != i + 1):
            ket_qua.append(f"x_{i+1} = t (ẩn tự do)")
            continue
            
        terms = []
        if abs(tmp[0]) > 1e-10: 
            terms.append(f"{tmp[0]:.2f}")
            
        for k in range(1, n + 1):
            if abs(tmp[k]) > 1e-10:
                sign = "+" if tmp[k] > 0 else "-"
                val = f"{abs(tmp[k]):.2f}" if abs(abs(tmp[k]) - 1.0) > 1e-10 else ""
                terms.append(f"{sign} {val}t")
                
        bieu_thuc = " ".join(terms).strip()
        if bieu_thuc.startswith("+ "): 
            bieu_thuc = bieu_thuc[2:]
        elif not bieu_thuc:
            bieu_thuc = "0"
            
        ket_qua.append(f"x_{i+1} = {bieu_thuc}")
        
    return ket_qua