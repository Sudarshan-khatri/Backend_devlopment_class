employe_data=[
    {'name':"ram",'salary':35000, 'bonous':2},
    {'name':"shyam","salary":45000,'bonous':5},
    {'name':"gopal","salary":67000,'bonous':6}
]

def bonus(sly,bon):
    bonus=sly+(sly*0.10)
    print(f"bonus:{bonus}")
for employee in employe_data:
    employ_name=employee['name']
    employ_salary=employee['salary']
    employee_bonus=employee['bonous']
    bonus(employ_salary,employee_bonus)
    

