def back_substitution(U: list, c: list):
    EPS = 1e-10

    m = len(U)
    if m == 0: return []
    n = len(U[0])

    # Khởi tạo dictionary x[i] = {0: hằng_số, k: hệ_số_của_x_k}
    x = [{} for _ in range(n)]

    # Mặc định mọi ẩn ban đầu đều là ẩn tự do.
    for i in range(n):
        x[i][i + 1] = 1.0

    for i in range(m - 1, -1, -1):
        
        # Tìm pivot khác 0 đầu tiên trên dòng i
        p = -1
        for j in range(n):
            if abs(U[i][j]) > EPS:
                p = j
                break

        # Kiểm tra hpt
        if p == -1: # Nếu cả dòng toàn số 0
            if abs(c[i]) > EPS: 
                raise ValueError("Hệ vô nghiệm") 
            continue 

        # Tính x[p]
        inv_pivot = 1.0 / U[i][p] 
        
        # Biểu thức mới của x[p], bắt đầu bằng phần hằng số: c_i / U_ip
        new_xp_expr = {0: c[i] * inv_pivot}

        # Thế các ẩn đã biết ở dưới lên
        for j in range(p + 1, n):
            val_ij = U[i][j]
            if abs(val_ij) > EPS:
                
                factor = -val_ij * inv_pivot
                
                for var_idx, weight in x[j].items():
                    current_weight = new_xp_expr.get(var_idx, 0.0)
                    updated_weight = current_weight + (factor * weight)
                    
                    if abs(updated_weight) > EPS:
                        new_xp_expr[var_idx] = updated_weight
                    elif var_idx in new_xp_expr:
                        del new_xp_expr[var_idx]

        x[p] = new_xp_expr

    #Khởi tạo nghiệm
    ket_qua = []
    for i in range(n):
        expr = x[i]
        
        # Xét xem x_i có phải ẩn tự do không
        is_free = (len(expr) == 1 and (i + 1) in expr and abs(expr[i + 1] - 1.0) < EPS)
        if is_free:
            ket_qua.append(f"x_{i+1} (ẩn tự do)")
            continue

        terms = []
        # Xử lý hằng số
        if abs(expr.get(0, 0.0)) > EPS:
            terms.append(f"{expr[0]:.2f}")

        # Sort keys để x1, x2, x3 in ra đúng thứ tự
        for k in sorted(expr.keys()):
            if k == 0: continue
            
            val = expr[k]
            sign = "+" if val > 0 else "-"
            abs_val = abs(val)
            
            # Nếu hệ số là 1 hoặc -1 thì ẩn đi
            formatted_val = f"{abs_val:.2f}" if abs(abs_val - 1.0) > EPS else ""
            
            if not terms: # Nếu đây là phần tử đầu tiên của chuỗi
                prefix = "-" if sign == "-" else ""
                terms.append(f"{prefix}{formatted_val}x_{k}")
            else:
                terms.append(f"{sign} {formatted_val}x_{k}")

        bieu_thuc = " ".join(terms).strip()
        if not bieu_thuc:
            bieu_thuc = "0"
            
        ket_qua.append(f"x_{i+1} = {bieu_thuc}")

    return ket_qua
