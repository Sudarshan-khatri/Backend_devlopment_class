def is_prime(nm):
    if nm>1:
        for i in range(2,nm):
            if(nm%i==0):
                return False
            
        return True
# user input to find the number is prime or composite
num=int(input("Enter Number:"))
print(f"prime:{is_prime(num)}")