n=(input("enter a number"))
l=""
t=""
for i in n:
    if i not in l:#or if n not in l:

        l+=i
        r= n.count(i)
        if r==1:
            t=t+i
           # print(i,end="")

print(len(t)," : number is unick that number is : ",t)
