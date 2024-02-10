big_tech = ["Apple","Amazon","Microsoft","Google","Meta","TESLA"]
print(big_tech)
big_tech.append("DELL") #used to add an element ina list at any place 
print(big_tech)
big_tech.insert(2,"HP") #used to add a element at a proper index
print(big_tech)
laptop = ["Alienware","Mac"]
big_tech.extend(laptop) #used to add another list
print(big_tech)
big_tech.remove("Microsoft") # used ot remvoe element by name
print(big_tech)
big_tech.pop(3) #used to remove element by its index number 
print(big_tech)
big_tech[3] = "Samsung" # used to replace element
print(big_tech)
big_tech.sort() #used to print in ascending oreder
print(big_tech)
big_tech.sort(reverse = True) #used to print in descending oreder
print(big_tech)
big_tech.reverse() #this is used to reverse a list
print(big_tech)
