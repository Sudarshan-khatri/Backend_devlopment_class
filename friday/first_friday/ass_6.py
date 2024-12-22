"""Write a program that checks if a given
word is a palindrome (reads the same
forwards and backwards).
Example Input: "madam"
Example Output: "madam is a palindrome"
Other words: racecar, level.."""

def str_pallindrome(word):
    str=word[::-1]
    if str==word:
        return (f"{word} is pallindrome")
    else:
        return (f"{word} is not pallindrome")
    
# user input to find the  given word is pallindrome 
wrd=input("Enter word:")
print(f"{str_pallindrome(wrd)}")