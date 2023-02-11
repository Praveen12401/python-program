l=int(input('enter starting point'))
h=int(input('enter ending point '))
a,b=[],[]

for n in range(l+1,h):
    status=False
    for i in range(2,n):
        if n%i==0:
            status=True

    if status:
        #not mprime ke liye
       #b.append(n)
     print('')

    else:
        #prime ke liye
        a.append(n)
print("prime number:-")
print(a)
print(" not prime number :- ")
print(b)

