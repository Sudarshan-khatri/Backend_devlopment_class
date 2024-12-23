class calculator:
    def sum(self,num1,num2):
        return num1+num2
    
    def sub(self,num1,num2):
        return num1-num2
    def prod(self,num1,num2):
        return num1*num2
    
    def div(self,num1,num2):
        return num1/num2
    
first_obj=calculator()
nm_1=int(input("Enter first number:"))
nm_2=int(input("Enter second number:"))
print(f"sum of two num:{first_obj.sum(nm_1,nm_2)}")
print(f"sub of two num:{first_obj.sub(nm_1,nm_2)}")
print(f"Prod of two num:{first_obj.prod(nm_1,nm_2)}")
print(f"Division of two num:{first_obj.div(nm_1,nm_2)}")

