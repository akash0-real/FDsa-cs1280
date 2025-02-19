def sum(n):
    if n<10:
        return n
    else:
        return n%10 + sum(n//10)
    
n = int(input("enter a value: "))
add = sum(n)
print(f"sum of number {n} is {add}")    
