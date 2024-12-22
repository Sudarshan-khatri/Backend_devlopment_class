num="0123456789"
highest=0
for num in range(len(num)):
     if int(num)> highest:
         highest=num

print(highest)

low=[]
for num in range(len(num)):
     if int(num)<low:
          low=num
print(low)
           
