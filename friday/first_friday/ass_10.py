"""Write a Python program that takes a
number as input and checks whether it
is positive, negative, or zero.
Example Input: -5
Example Output: "The number is
negative”"""

def number_checker(num):
    if num<0:
        return -1
    elif num==0:
        return 0
    elif num>0:
        return 1
    
# user input to check the number is positive ,negative or equall to zero 
user_num=int(input("Enter number:"))
check=number_checker(user_num)
if check==-1:
    print(f"{user_num} is negative")
elif check==0:
    print(f"{user_num} is zero")
elif check==1:
    print(f"{user_num} is positive")