big_tech = ["Apple","Amazon","Microsoft","Google","Meta","TESLA"]
#print(big_tech)
big_tech.insert(2,["HP","Lenovo"]) 
print(big_tech[2][0]) #it asks for the 2 indexed element in the list , which is itself a list , so it will print that list , so now we will have to tell about the particular element in that list . Like big_tech[2][0] will give us HP. 

#new_tech = [big_tech for big_tech in big_tech if "A" in big_tech]
#print(new_tech)
