"""Write a program that prints the following
pattern:
*
**
***
****
*****"""
row=5
for i in range(row+1):
    for j in range(i):
        print("*",end='')

    print('')
    