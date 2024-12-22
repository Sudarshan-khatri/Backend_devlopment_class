"""Write a Python function that takes a string as
input and returns a dictionary where the keys
are the words in the string, and the values are
the lengths of those words.
Example Input: "Hello world from Python"
Example Output: {'Hello': 5,
'world': 5,
'from':
4,
'Python': 6}"""

def str_to_dict_converter(word):
    str_1=word.split()
    for i in range(int(str_1)):
        print(len(str_1))


# enter the string to convert into dictionary
str=input("Enter string:")
str_to_dict_converter(str)