a = int(input("enter a :"))
b = int(input("enter b : "))
operator = input("enter the operator :")
match operator:
     case "+":
        print("your addition is : ",a+b)
     case "-":
         print("your subtraction is : ",a-b)
     case "*":
         print("your product is : ",a*b)
     case "/":
         print("your division is : ",a/b)
     case _:
         print("please enter a valid")