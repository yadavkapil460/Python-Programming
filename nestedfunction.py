def outerfunction():
    x = 8
       
    def innerfunction():
       y = 2
       result = x+y
       return result
           
    return innerfunction()
output = outerfunction()
print(output)