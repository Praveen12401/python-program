n=int (input("Enter a number "))
n1=(input("Enter a number "))
try:

    a=n/n1
    print("this number ",a)
except Exception as i:

    print( "this number",i,f"{n},{n1} do  not work")
else:
    print("else block ")
