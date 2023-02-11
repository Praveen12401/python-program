row=int(input('enter row'))
col=int (input('enter collom'))
mat=[]
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input('enter a number')))

        mat.append(a)
for i in range(row):
    for j in range(col):
        print(mat[j][i],end=" ")
    print(' ')