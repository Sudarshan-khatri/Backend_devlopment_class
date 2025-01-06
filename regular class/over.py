class masu:
    # def __init__(self,id,name,weight):
    #   self.id=id
    #   self.name=name
    #   self.weight=weight
    def intro(self):
       print(f"id:{self.id}")
       print(f"Name:{self.name}")
       print(f"Weight:{self.weight}")

    def taste(self):
       print("Hello iam student of vrit skill")

class type(masu):
   def taste(self):
        choice=int(input("Enter the choice:"))
        if(choice==1):
           print("So tasty")
        elif(choice==2):
           print("Thik Thak")
        elif(choice==3):
           print("out of range")
        elif(choice==4):
         print("Nice")


 
print("1:Khasi")
print("2:Buff")
print("3:Chicken")
print("4:Local chicken")
# detail of meat  
id_1=int(input("Enter the id:"))
name_1=input("Enter the name:")
weight_1=int(input("Enter the weight:"))   
# create a object of class type
obj_1=type(id_1,name_1,weight_1)
obj_1.intro()
obj_1.taste()
      

     
