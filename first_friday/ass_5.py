"""Write a program that takes a string as
input and prints the string in reverse
order.
Example Input: "Python"
Example Output: "nohtyP"""
def str_reverse(word):
    word=word[::-1]
    return word

# user input to find the reverse of string 
letter=input("Enter the word:")
print(f"word in reverse:{str_reverse(letter)}")