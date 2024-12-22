"""Write a program that calculates the
factorial of a given number n (where n
is provided by the user).
Example Input: n = 5
Example Output: Factorial = 120
(because 5! = 5×4×3×2×1 = 120)"""

def factorial(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*(factorial(num-1))
    

# user input to find the factorial 
number=int(input("Enter number:"))
print(f"factorial of {number}:{factorial(number)}")