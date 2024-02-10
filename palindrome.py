string = input("please enter a string : ")
output = string[::-1]
print("your original string was : ",string)
print("your reversed string is : ",output)
if string == output :
    print("your string is a palindrome")
else :
    print("your string is not a palindrome")
