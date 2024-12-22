"""Write a program that takes a number n
as input and prints the square of all
numbers from 1 to n.
Example Input: n = 4
Example Output: 1^2 = 1, 2^2 = 4, 3^2 =
9, 4^2 = 16"""

def square(num):
    return num**2

# input the number to find the square 
term=int(input("Enter the term:"))
for i in range(term):
    sq_num=int(input("Enter number"))
    print(f"square of {sq_num}: {square(sq_num)}")