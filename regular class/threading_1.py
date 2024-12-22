import threading
import time
def sum():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    time.sleep(5)
    print(f"sum:{a+b}") 
    
def prod():
    c=int(input("Enter first number:"))
    d=int(input("Enter second number:"))
    time.sleep(5)
    print(f"prod:{c*d}") 

t1=threading.Thread(target=sum)
t2=threading.Thread(target=prod)
t1.start()
t1.join()
t2.start()
t2.join()