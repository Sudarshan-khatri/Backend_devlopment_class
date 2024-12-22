"""Write a Python program that takes a list of students'
names and their corresponding marks in a subject, stores
them in a dictionary, and then calculates and prints the
average mark.
Example Input: ['Alice'
,
'Bob'
,
'Charlie'] and [85, 92,
78]
Example Output: {'Alice': 85,
'Bob': 92,
'Charlie': 78}
and Average = 85"""

def comprise(name,marks):
    student_record=dict(zip(name,marks))
    return (student_record)

def average_mark(mrks):
    sum=0
    for i in range(len(mrks)):
        sum+=mrks[i]
    return (sum/len(mrks))



student=[]
mark=[]
number_student=int(input("\n\n Enter student number:"))
for i in range(number_student):
    stud_name=input(f"\nEnter student_name_{i+1}:")
    student.append(stud_name)
    stud_mark=int(input(f"Enter student mark_{i+1}:"))
    mark.append(stud_mark)
print(f"STUDENT RECORD:\n{comprise(student,mark)}")
print(f"Average mark:{average_mark(mark):.2f}")

