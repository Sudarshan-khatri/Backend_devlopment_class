# calculator that perform operation on two operand using full functionality
def operation(nm1,nm2):
    opt=input(f"Enter the operation(+,-,*,/,%):")
    if opt=="+":
        return int(nm1+nm2)
    elif opt=="-":
        if nm1>nm2:
            return nm1-nm2
        else:
            return nm2-nm1
    elif opt=="*":
        return nm1*nm2
    elif opt=="/":
        if nm1>nm2:
            return int(nm1/nm2)
        else:
            return int(nm2/nm1)
    elif opt=="%":
        if nm1>nm2:
            return nm1%nm2
        else:
            return nm2%nm1
        
# define the user input data and call the function:
data_1=int(input(f"Enter first number:"))
data_2=int(input(f"Enter second number:"))
print(f"Result:{operation(data_1,data_2)}")
        