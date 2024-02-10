n = int(input("enter n : "))
if n % 15 == 0 :
    print("your number is divisible by 15")
    if n%3==0 and n%5==0 :
         print("number is divisible by 3 and 5")
    else : 
         print("not divisible by 3 and 5")
else : 
    print("neither divisible by 3,5 ,15")
