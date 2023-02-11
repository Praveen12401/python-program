n=int(input("enter a binary number"))
c=n
pow=0
sum=0
while n>0:
    r=n%10
    sum=sum+(2**pow)*r
    n=n//10
    pow+=1
print(c,"of decimal number",sum)
