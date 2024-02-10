n = int(input("enter the size of list : "))

list = []
for _ in range(n):
    num = int(input())
    list.append(num)
    
idx1 = int(input("enter the first index : "))
idx2 = int(input("enter the second index : "))

temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)