#factorial of a number 
n = int(input("Enter a number : "))
factorial = 1
if n<0 :
    print("your factorial doesn't exist")
elif n==0 :
    print("your factorial is 1")
else :
 for i in range(1,n+1):
    factorial *= i
    
    
print("your factorial of",n,"is",factorial)    
print()