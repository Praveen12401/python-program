# a="praveen"
# new_string= a[:3]+"d"+a[4:-1]+"p"
# print(new_string)
# print(a)

def exchan(a):
    start_number = a[0]
    last_number = a[-1]
    exchange = last_number + a[1:-1] + start_number
    print(exchange)
a=input("enter a string data : ")
exchan(a)