input_tuple = (1,2,3,4,4,5)

list = []

for _ in reversed(input_tuple):
    list.append(_)
    
output_tuple = tuple(list)
print("reversed tuple is : ",output_tuple)