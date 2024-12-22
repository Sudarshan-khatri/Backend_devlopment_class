def square(num1,num2):
    operation=input(f"Enter the operation:")
    if operation=="+":
        return num1+num2
    elif operation=="-":
        return num1-num2
    elif operation=="*":
        return num1*num2
    else:
        return num1/num2
    

nm1=int(input(f"Enter first number:"))
nm2=int(input(f"Enter second number:"))
print(square(nm1,nm2))
