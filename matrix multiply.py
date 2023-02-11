matrix_2=[]
matrix_1 = []
matrix_3=[]
row_1=int(input("enter row number of first matrix : "))
colmn_1=int(input("enter colomn number of first matrix : "))
def first_matrix(row_1,colmn_1):


    for i in range(row_1):
        A=[]
        for j in range(colmn_1):
            x=int(input("enter a number"))
            A.append(x)
        matrix_1.append(A)
    print(" this is your first matrix here : ")
    print(matrix_1)
#first matrix call here
first_matrix(row_1,colmn_1)

#second matrix code start here
row_2=int(input("enter row number of first matrix : "))
colmn_2=int(input("enter colomn number of first matrix : "))
def second_matrix(row_2,colmn_2):

    for i in range(row_2):
        B=[]
        for j in range(colmn_2):
            x=int(input("enter a number"))
            B.append(x)
        matrix_2.append(B)
    print(" this is your second matrix here : ")
    print(matrix_2)
#second matrix call here
second_matrix(row_2,colmn_2)

#two matrix multiply code here
def multiply_matrix(row_2,colmn_2,colmn_1,row_1,matrix_1,matrix_2,matrix_3):
    if colmn_1 != row_2:
        print("not posible multiply because first matrix colmn not equal second matrix row ")
        return

    D = [[0 for i in range(row_1)]
         for j in range(colmn_2)]
    for i in range(row_1):

        for j in range(colmn_2):



            for k in range(row_2):
                D[i][j] += matrix_1[i][k] * matrix_2[k][j]

    print("this is here multiply matrix")
    print(D)
#call multiply matrix here
multiply_matrix(row_2,colmn_2,colmn_1,row_1,matrix_1,matrix_2,matrix_3)

























