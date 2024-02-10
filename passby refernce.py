def modify(lst):
    lst.append(4)
    print("inside function : ",lst)

lst = [1,2,5]
modify(lst)
print("outer function : ",lst)