a=int(input('enter first number'))
b=int(input("enter second number"))
if a>b:
   s=a
else:
   s=b
for i in range(2,s):890
   if a%i==0 and b%i==0:
      hcf=i
#print('hcf:',hcf)
lcm=(a*b)/hcf
print('lcm',lcm,'\t', 'hcf',hcf)



