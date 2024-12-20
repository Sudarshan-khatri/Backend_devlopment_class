"""
The map() function executes a specified function for each item in an iterable.
 The item is sent to the function as a parameter.

Syntax
map(any_function, iterables)
"""

number=(9,2,3,4,5,6,7,8,9,0)
squared=tuple(map(lambda x:x**2,number))
print(squared)

number=[1,2,4,6,4,3,6,7,8,9]
cube=list(map(lambda x:x ** 3, number))
print(cube+number)