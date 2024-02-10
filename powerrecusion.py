def power(a,b):
    if a==0:
     return 1
    
    elif b==0:
     return 0
     
    else :
        return b ** a
a = int(input("enter a : "))
b = int(input("enter b : "))
result = power(a,b)
print(result)
    
    