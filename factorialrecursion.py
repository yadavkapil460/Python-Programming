def calc_fact(n):
    
    if n==0:
        return 1
        
    ans  = n * calc_fact(n-1)
    return ans
    
n = int(input("enter n " ))
print(calc_fact(n))