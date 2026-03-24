def back_substitution(U: list, c : list):
    n=len(c)
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        if U[i][i]==0:
            raise("Phần tử trên đường chéo chính bằng 0, không thể giải")
        sum=0.0
        for j in range(i+1,n):
            sum+=U[i][j]*x[j] #x[j] là nghiệm tìm đc bên dưới
        x[i]=(c[i]-sum)/U[i][i]
    return x

#test
U=[[1,2,3],[0,1,2],[0,0,2]]
c=[9,4,3]
x=back_substitution(U,c)
print("Nghiệm của phương trình là:")
print(x)