n=int(input("Enter number:"))
list=[]
for i in range(n):
    value=int(input(""))
    list.append(value)
    

list_1=set(list)
list_2=sorted(list_1)
print(f"output:{list_2[-2]}")