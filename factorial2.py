def calc_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    return factorial
    
n = int(input("enter n : "))
output = calc_factorial(n)
print(output)
