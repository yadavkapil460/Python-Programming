'''fruit = {"apple","mango"}
for _ in fruit:
    print(_)
    
fruit.add("guava")
print(fruit)

new_fruits = ["litchi","orange"]
fruit.update(new_fruits)
print(fruit)

fruit.remove("apple")
fruit.discard("mango")
print(fruit)

s1 = {'q','w','e','r','t','y'}
s2 = {'a','s','e'}
s1.update(s2)
print(s1)

s3 = s1.union(s2)
print(s3)'''

s1 = {'q','w','e','r','t','y'}
s2 = {'a','s','e'}
'''s1.intersection_update(s2)
print(s1)'''

s1.symmetric_difference_update(s2)
print(s1)





