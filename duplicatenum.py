#take two sets as input and tell which elements are duplicate
m = int(input("enter the size of the first set: "))
n = int(input("enter the size of second set : "))
set1list = []
for _ in range(m):
  num1 = input(f"enter the {_+1} element of first set :")
  set1list.append(num1)

set1 = set(set1list)
print("your set 1 is: ",set1)

set2list = []
for _ in range(n):
  num2 = input(f"enter the {_+1} element :")
  set2list.append(num2)

set2 = set(set2list)
print("your second set is : ",set2)

set1.intersection_update(set2)
print("only these values are duplicate",set1)