Phone_Numbers = {
    "John" : 88657346987,
    "Jack" : 37543698758,
    "William" : 599875615614,
    "Green" : 9845156486515,
}
print(Phone_Numbers["Jack"])
print(Phone_Numbers.values())

Phone_Numbers["Williamson"] = 5774618678
Phone_Numbers["John"] = 3757345755
print(Phone_Numbers["John"])
print(Phone_Numbers)

more_numbers = {
    "Kia" : 985864419897984,
}
Phone_Numbers.update(more_numbers)
print(Phone_Numbers)
