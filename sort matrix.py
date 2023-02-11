
row=int(input("enter row number : "))
colmn=int(input("enter colmnnumber : "))
def M(colmn,row):
    matrix_list = []
    for i in range(row):
        A = []
        for j in range(colmn):
            x = int(input("enter anumber :  "))
            A.append(x)
        matrix_list.append(A)
    for i in matrix_list:
        print(i)
M(colmn,row)

