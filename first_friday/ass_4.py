"""Write a Python program that takes a
positive integer as input and
calculates the sum of its digits.
Example Input: 1234
Example Output: Sum of digits = 10"""

def digit_sum(num):
    sum=0
    while num>0:
        sum+=(num%10)
        num=num//10
    return int(sum)

# user input the number
num_1=int(input("Enter number:"))
print(f"sum of digitss:{digit_sum(num_1)}")
      