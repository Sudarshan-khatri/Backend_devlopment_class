# function to find the number is odd or even 
def checker(num):
    if num%2==0:
        return True
    else:
        return False
    
# number to find the given number id true or false
nm=int(input("Enter number:"))
check=checker(nm)
if check==True:
    print(f"{nm} is even")
else:
   print(f"{nm} is odd") 