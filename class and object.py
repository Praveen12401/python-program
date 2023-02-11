class A:
    def d(self):
        print("hello")
        a = 3
        b = 41
        print(a + b)
# t=A()
print(A.d("self"))
def fun(*arg,**kwargs):
    for i in arg:

        print(i)
    for key in kwargs:
        print(key,":",kwargs[key])
list_1=[1,2,38,4,5,7]

dic={"h":10,"ram":"radha"}
fun(*list_1,**dic)
a="ram go to home"
n=" and house"
p=f"{a}{n}"
print(p)
# a=70
# print(id(a))
# b=70
#
# print(id(b))
# a=a+8
# print(a,id(a))
# b+=2089
# print(b,id(a))