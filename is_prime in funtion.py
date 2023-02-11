def is_prime(l,u):
    A=[]
    B=[]
    a=[]
    b=[]
    if l<2:
        return
    for n in range(l,u+1):
        status=False
        for i in range(2,n):
            if n%i==0:
                status=True
        if status:
                # this is not prime number
            A.append(n)





        else:
                #this is prime number
            B.append(n)
            for j in range(2, n):
                if n % j == 0:
                    b.append(j)
    print('this is not prime number',A,'\n',a)
    print('this is not prime number',B,'\n',b)

l=int(input('enter lowest limit'))
u=int(input('enter upper limit'))
is_prime(l,u)




