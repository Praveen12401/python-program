# a=open("smaaple.text","r+")
# r=a.write("hello new file \n")
# print(a)

n=(input("enter your name : "))
a=(input("enter a age : "))
with open("sample.text","a+") as t:
    t.write("name : ")
    t.write(n)
    t.write("\n")
    t.write("age : ")
    t.write(a)
    t.write("\n")
print(t.open)

print(t.close)
print(t.open)



# r=t.read()
# print(r)