class personal_information:
    def __init__(self,name,cast,level,dob,h_status):
        self.name=name
        self.cast=cast
        self.level=level
        self.dob=dob
        self.h_status=h_status
    
    def infor(self):
        return self.name,self.cast,self.level,self.dob,self.h_status
    
# user defined information used given by user
name=input("Enter name:")
cast=input("Enter cast:")
level=input("Enter level:")
db=input("Enter date of birth:")
hstat=input("Enter health status:")
# create a object of personal information class 
info_obj=personal_information(name,cast,level,db,hstat)
print(f"Personal information\n")
print(f"{info_obj.name}") 
print(f"{info_obj.cast}") 
print(f"{info_obj.level}") 
print(f"{info_obj.level}") 
print(f"{info_obj.h_status}") 

    