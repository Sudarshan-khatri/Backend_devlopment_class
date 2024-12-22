"""Write a program that finds the highest
and lowest digit in a given string of
numbers.
Example Input: "0124392566"
Example Output: Highest = 9, Lowest = 0"""

def highest(num):
    high=0
    for num in range(len(num)):
        if int(num)>high:
            high=num
    return high
# function to find the lowest number
def lowest(num):
    low=int(num[0])
    for num in range(len(num)):
        if int(num) < low:
            low=num
    return low

        
# define number and call the  function
input="0123456789"
print(f"highest number:{highest(input)}")
print(f"Lowest number:{lowest(input)}")
    
