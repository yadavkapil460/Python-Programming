n = int(input("enter the size of set : "))
numbers = []

for _ in range(n):
    number = input(f"enter {_ + 1} :")
    numbers.append(number)
    
output = set(numbers)
print("your final set is : ",output)