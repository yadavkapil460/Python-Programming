def sumofall(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
output = sumofall(2,3,4,5,678)
print("sum of all is : ",output)