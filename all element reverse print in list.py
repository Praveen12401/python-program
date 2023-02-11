list_1=[1,'ram','praveen',2,3,'shyam']
store_data_reverse_of_list=[]
reverse_of_list=[]
c=len(list_1)
for i in range(-1,-c-1,-1):
    reverse_of_list.append(list_1[i])
    print(i,end=" ")

print('')
# l.reverse()
# l.sort()
print(reverse_of_list)
print('')
# t='praveen'
# print(t[-1::-1])
# 1
# a=12345
#print((str(a)),str(a)[-1::-1])
for i in reverse_of_list:
    #i=str(i)
    store_data_reverse_of_list.append(str(i)[-1::-1])
print(store_data_reverse_of_list)
