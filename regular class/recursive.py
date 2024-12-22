data =[]
def sum(n):
    while n<10:
        data.append(n)
        return sum(n+1)
    return data
   

print(f"sum:{sum(0)}")

