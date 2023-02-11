# # addition=lambda x,y:x*y
# # print(addition(2,5))
# for i in range(65,90):
#     print(chr(i),end="   ")
n=int(input("enter a number "))
for i in range(1,11):
    for j in range(1,n+1):
        print(i*j,end=" \t")
    print("")
