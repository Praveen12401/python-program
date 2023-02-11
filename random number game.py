import random
n=random.randint(1,10)
count=0
status =1
while status<=5:
    try:
        x=int(input("enter a number from 1 to 10  : "))
        if x==n:
            count+=1
            print("number is match")

            break


        elif x>n and x<=10:
            count+=1
            print("high your number,again enter number")
        elif x<n and x>0:
            count += 1
            print("low your number,again enter number")
        elif x>n or x<n:
            count += 1
            print("out of range input")
    except :
        print("invailid input")
    status+=1
print("your try chance attemp",count)
