start=int(input("enter first number"))
end=int(input("enter second number"))
'''if start%2==0:
    start+=2'''
if start%2!=0:
    start+=1
for items in range(start,end,2):
    print(items)
