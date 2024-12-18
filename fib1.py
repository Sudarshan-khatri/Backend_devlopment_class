first_term=0
second_term=1
term=int(input("Enter the term:"))
print(first_term)
print(second_term)
for i in range(2,term):
    next_term=first_term+second_term
    print(next_term)
    first_term=second_term
    second_term=next_term
   
