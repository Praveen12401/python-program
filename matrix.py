row=int(input("How many row enter"))
colomn=int(input("How many colmn enter"))
matrix=[]
for i in range(row):
    a=[]
    for j in range(colomn):
        a.append(int(input("enter a number : ")))
    matrix.append(a)
for i in range(row):
    for j in range(colomn):
        print(matrix[i][j],end="  ")

    print("")

