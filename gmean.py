def Gmean(a,b):
    mean = (a+b)/(a*b)
    return(mean)
a = int(input("enter a : "))
b =int(input("enter b :  "))
gmean1 = Gmean(a,b)
print("your geometric mean is  :",gmean1)
#value nikalte time hame jo naam humne function ko diya h , use hi likhna h like result= Name_function(x,y) or pehle se humne us functoin ko define kr rkha hota h like from line 1 to 3 here to jb hm  result k liye Name_function me value daalenge to vo value sidha us function ke formula me chli jyegi or hume output mil jayega
m = int(input("enter m : "))
n =int(input("enter n :  "))
gmean2 = Gmean(m,n)
print("your second geometric mean is  :",gmean2)