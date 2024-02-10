#printing numbers n to 1
def print_numbers(n):
  if n==0:
    return 0
  elif n!=0:
   for i in range(n,0,-1):
    print(i)
  return i

n = int(input("Enter n : "))
print_numbers(n)