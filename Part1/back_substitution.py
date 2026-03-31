def back_substitution(U: list, c: list):
    m = len(U)
    if m == 0: return []
    n = len(U[0])

    x = [[0.0] * (n + 1) for _ in range(n)]

    for i in range(n):
        x[i][i + 1] = 1.0

    for i in range(m - 1, -1, -1):
        p = -1
        for j in range(n):
            if abs(U[i][j]) > 1e-10:
                p = j
                break

        if p == -1:
            if abs(c[i]) > 1e-10:
                return "Hệ vô nghiệm"
            continue

        x[p] = [0.0] * (n + 1)
        x[p][0] = c[i] / U[i][p]

        for j in range(p + 1, n):
            if abs(U[i][j]) > 1e-10:
                factor = -U[i][j] / U[i][p]
                for k in range(n + 1):
                    x[p][k] += factor * x[j][k]

    # Lọc các ẩn tự do
    free_vars = [i for i in range(n) if abs(x[i][i + 1] - 1.0) < 1e-10 and all(abs(x[i][k]) < 1e-10 for k in range(n + 1) if k != i + 1)]

    # Trường hợp vô số nghiệm 
    if free_vars:
        x0 = [row[0] for row in x]  # Nghiệm riêng ban đầu
        N = [[row[j + 1] for row in x] for j in free_vars]  # Các vector cơ sở
        k = len(free_vars)

        # Tính ma trận vuông (N * N^T) và vector (-N * x0) để tìm trọng số t
        Nt_N = [[sum(N[i][l] * N[j][l] for l in range(n)) for j in range(k)] for i in range(k)]
        Nt_x0 = [-sum(N[i][l] * x0[l] for l in range(n)) for i in range(k)]


        for i in range(k):
            pivot = max(range(i, k), key=lambda r: abs(Nt_N[r][i]))
            Nt_N[i], Nt_N[pivot] = Nt_N[pivot], Nt_N[i]
            Nt_x0[i], Nt_x0[pivot] = Nt_x0[pivot], Nt_x0[i]

            if abs(Nt_N[i][i]) > 1e-10:
                for j in range(i + 1, k):
                    factor = Nt_N[j][i] / Nt_N[i][i]
                    for l in range(i, k):
                        Nt_N[j][l] -= factor * Nt_N[i][l]
                    Nt_x0[j] -= factor * Nt_x0[i]

        t = [0.0] * k
        for i in range(k - 1, -1, -1):
            if abs(Nt_N[i][i]) > 1e-10:
                t[i] = (Nt_x0[i] - sum(Nt_N[i][j] * t[j] for j in range(i + 1, k))) / Nt_N[i][i]

        # Tính nghiệm chuẩn nhỏ nhất = x0 + N^T * t
        min_norm_x = [round(x0[i] + sum(N[j][i] * t[j] for j in range(k)), 6) for i in range(n)]

        return ["Vô số nghiệm", min_norm_x]

    # Trường hợp nghiệm duy nhất
    ket_qua = []
    for i in range(n):
        tmp = x[i]
        if tmp[i + 1] == 1.0 and all(abs(tmp[k]) < 1e-10 for k in range(n + 1) if k != i + 1):
            ket_qua.append(f"x_{i+1} (ẩn tự do)")
            continue

        terms = []
        if abs(tmp[0]) > 1e-10:
            terms.append(f"{tmp[0]:.2f}")

        for k in range(1, n + 1):
            if abs(tmp[k]) > 1e-10:
                sign = "+" if tmp[k] > 0 else "-"
                val = f"{abs(tmp[k]):.2f}" if abs(abs(tmp[k]) - 1.0) > 1e-10 else ""
                terms.append(f"{sign} {val}x{k}")

        bieu_thuc = " ".join(terms).strip()
        if bieu_thuc.startswith("+ "):
            bieu_thuc = bieu_thuc[2:]
        elif not bieu_thuc:
            bieu_thuc = "0"

        ket_qua.append(f"x_{i+1} = {bieu_thuc}")

    return ket_qua
