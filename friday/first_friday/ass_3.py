"""Write a program that takes a sentence
as input and counts the number of words
in it.
Example Input: "Python is fun"
Example Output: Number of words =3"""

def no_count(str):
   str_1=str.split()
   print(len(str_1))

# user input to count the word in the paragraph
word=input("Enter the paragraph:")
no_count(word)