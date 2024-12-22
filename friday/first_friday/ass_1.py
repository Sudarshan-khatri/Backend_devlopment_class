"""Write a Python program that asks the
user to input a number and then
prints whether the number is even or odd"""

def checker(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# user defined input given by the user 
num_1=int(input("Enter number to check even or odd:"))
checker(num_1)