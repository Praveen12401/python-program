# l=input("enter a list(string) from sample [112bsh38sa]: ")#output: ahss11238
# A=[]
# B=[]
# for i in l:
#     if i.isalpha():
#         A.append(i)
#     else:
#         # i=int(i)
#         B.append(i)
# C=sorted(A)+(sorted(B))
#
# print("".join(C))
# print("hello")
# words=input("enter a string and number: ")#input a2b4c7   output aabbbbccccccc
#
# A=[]
# for char in words:
#     if char.isalpha():
#         r=char
#     else:
#         A.append( r*int(char))
# Z="".join(A)
# print(Z)
# wordes=input("enter a string :")#ff gg ss dd g ff
# #who are string repeated
#
# A=wordes.split()#output : ff
# list1=[]
# B=[]
# for i in A:
#     n=0
#     if i not in list1:
#
#         list1.append(i)
#         n=A.count(i)
#     if n>=2:
#         B.append(i)
# l=len(B)
# if l ==0:
#     print("NA")
# else:
#
#     print("".join(B))
import operator as o
def dec(fun):
    def exee():
        print("good morning ")
        print("your addition :",end="")
        fun()
        print("good night ")
    return exee
@dec
def pra():
    print(o.add(10,20))
pra()
print("hello everyone")








