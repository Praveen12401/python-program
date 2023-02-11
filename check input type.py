def check(x):
    try:
        a=int(x)
        print("this value integer ",a)
    except:
        try:
            b=float(x)
            print("this value float ",b)
        except:
            try:
                c=str(x)
                print("this value string ",c)
            except:
                print("good")
x=input("enter a value : ")
check(x)