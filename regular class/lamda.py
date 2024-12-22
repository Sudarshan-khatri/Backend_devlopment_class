# A lambda function is a small anonymous function.A lambda function can take any number of
# arguments, but can only have one expression.



# lambda function to product any two number
product=lambda first_num,second_num:first_num*second_num

# function call 
f_num=float(input("Enter first number:"))
s_num=float(input("Enter second number:"))
print(product(f_num,s_num))