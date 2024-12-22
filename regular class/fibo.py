def fibo(nm):

    if nm==0:
        return 0
    elif nm==1:
         return 1   
    else:
        return fibo(nm-1)+ fibo(nm-2)
term=int(input("Enter term:"))
for i in range(term):       
  print(f"fibo series:{fibo(i)}")
    
    