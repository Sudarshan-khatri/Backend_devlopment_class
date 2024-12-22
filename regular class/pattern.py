""""
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
"""
print('\n\n')
# pattern to find the above of the structure
rows=5
for i in range(rows+1):
    for j in range(i):
        #print the i for this pattern
        print(i,end='')
    # end the line after every loop  
    print('')


"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
 """
print('\n\n')
# print the output of this format
rows=5
# use for loop to find the range 
for i in range(1,rows+1):
    for j in range(i):
        print(j+1,end='')
    # add the new line after every time 
    print('')

"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
"""
print('\n\n')
row=5
# print this format of pattern
for i in range(1,row+1):
    for j in range(i,row+1):
        print(i,end='')
    # end the line in every loop 
    print('')

"""
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""

print('\n')
# print the structure of above pattern
for i in range(1,row+1):
    for j in range(i,row+1):
       print(row,end='')
    # end the line in every loop 
    print('')
    
"""
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
"""
print('\n')
# print the format of above patterns:
for i in range(rows+1):
    for j in range(i,rows+1):
        print(i,end='')
    # end the line in every loop 
    print('')


