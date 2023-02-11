import operator as o
def dec(fun):
    def additional_functionality():
        print("good morning ")
        print("your addition :",end="")
        fun()
        print("good night ")
    return additional_functionality
@dec
def pra():
    print(o.add(10,20))
pra()
print("hello everyone")
