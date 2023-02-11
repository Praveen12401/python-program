
def s():
    global x
    x=6.9

    print(x)
    def t():
        global x

        print(x)
    t()
s()

print(x)