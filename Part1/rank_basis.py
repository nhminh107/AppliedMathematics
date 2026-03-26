def back_substitution(U,c):
    pass

from gaussian import gaussian_eliminate

def rank_and_basis(A):
    nRow = len(A)
    nCol = len(A[0])

    #Khử Gauss lấy ma trận bậc thang
    B = [0.0] * nRow
    augMatrix, _, _ = gaussian_eliminate(A, B)

    #Xác định rank và vị trí cac cột pivot
    pivotCol = []
    currRow = 0
    rank = 0
    for i in range(nCol):
        if currRow < nRow and abs(augMatrix[currRow][i]) > 1e-10:
            pivotCol.append(i)
            rank += 1
            currRow += 1

    #Cơ sở ko gian dòng
    rowBasis = [augMatrix[i][:nCol] for i in range(rank)]

    #cơ sở ko gian cột
    colBasis = []
    for i in pivotCol:
        basisColVector = [A[j][i] for j in range(nRow)]
        colBasis.append(basisColVector)

    #cơ sở ko gian nghiệm
    nullBasis = []
    #chứa các chỉ số cột ko phải pivot
    freeVars = [i for i in range(nCol) if i not in pivotCol]
    for f in freeVars:
        c = [0.0] * nRow
        specialSol = [0.0] * nCol
        specialSol[f] = 1.0
        #Gán biến tu do =1
        for i in range(rank):
            c[i] = -augMatrix[i][f]
            #Chuyển hệ so bien tu do sang vế phải

        #Xuất ma trận vuông từ các cột chốt
        reducedMatrix = []
        for i in range(rank):
            reducedRow = [augMatrix[i][j] for j in pivotCol]
            reducedMatrix.append(reducedRow)
        #Giải hệ để tìm giá trị các bien chốt
        pivotVal = back_substitution(reducedMatrix, c[:rank])

        for i in range(len(pivotCol)):
            pCol = pivotCol[i]
            val = pivotVal[i]
            specialSol[pCol] = val

        nullBasis.append(specialSol)

    return rank, rowBasis, colBasis, nullBasis
