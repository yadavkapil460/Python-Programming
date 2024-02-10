n = int(input("enter the size of the tupple you want to make :"))
numbers = []

for _ in range(n):
    number = input(f"enter a number {_ + 1} : ")
    numbers.append(number)
    
output = tuple(numbers)
print(output)
