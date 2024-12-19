# function to convert AD to BS 
def AD_to_BS(year,month,day):
    day=day+17
    if(day>30):
        month=(month+8)+(day/30)
        day=day%30
    if(month>12):
        year=(year+56)+(month/12)
        month=month%12
    print(f"Year:{int(year)}")
    print(f"Month:{int(month)}")
    print(f"Day:{int(day)}")

# function to convert bs to ad  
def BS_TO_AD(year,month,day):
    pass

# input entered by the user 
print("1:AD_TO_BS")
print("2:BS_TO_AD")
option=int(input("Enter option:"))
if option==1:
    y_r=int(input("Enter year:"))
    m_nt=int(input("Enter month:"))
    d_y=int(input("Enter day:"))
    AD_to_BS(y_r,m_nt,d_y)