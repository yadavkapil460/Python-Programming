def numbers(n):
    if n == 0:
        return  # Base case: Stop recursion when n reaches 0
    print(n)  # Print the current number
    numbers(n - 1)  # Make a recursive call with n - 1

n = int(input("Enter n: "))
numbers(n)  # Call the function with the provided input
