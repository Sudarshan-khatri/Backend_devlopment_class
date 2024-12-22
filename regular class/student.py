# project to store the student record the .Following the operation are necessary::
    # 1:Add student 
    # 2:show student details
    # 3:Search student 
    # 4:delete student 

# function to add the student datails
def add_student():
    s_num=int(input("Enter student Number to add the record:"))
    for i in range(s_num):
        s_name=input("Enter student name:")
        s_faculty=input("Enter the faculty:")
        s_id=int(input("Enter the id_no:"))
        s_roll=int(input("Enter the roll_number:"))
    print("\n\nSTUDENT INFORMATION")
    for i in range(s_num):
        print(f"\nStudent_name:{s_name}")
        print(f"Student_faculty:{s_faculty}")
        print(f"Student_id:{s_id}")
        print(f"Student_roll:{s_roll}")
#function to show the student details after add
def show_student():
    pass
#function to search the student details 
def search_student():
    pass
#function to delete the student details
def delete_student():
    pass



#make the software customize and give output:
print("\n\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n")
print("1:Add student")
print("2:show student details")
print("3:Search student")
print("4:delete student ")
admin_choice=int(input("\nchoose the operation:"))
if admin_choice==1:
    add_student()
elif admin_choice==2:
    show_student()
elif admin_choice==3:
    search_student()
elif admin_choice==4:
    delete_student()
else:
    exit(0)
