# recursive function to display square output
def square(nm):
    print(nm**2)
    if nm<15:
        square(nm+1)
square(1)
