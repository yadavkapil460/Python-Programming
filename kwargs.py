#here by using kwargs
'''def StudentInfo(**kwargs):
    for (x,y) in kwargs.items():
      print(x ,"is", y)
     
StudentInfo(name = "Kapil" , City = "Bawal" , MobileNumber = "9996547555" , Age = "18")
StudentInfo(name = "William" , City = "London" , MobileNumber = "5484946871" , Age = "28")
StudentInfo(name = "John" , City = "Los Angeles" , MobileNumber = "5789498197" , Age = "21")
StudentInfo(name = "Li Zhang" , City = "Shanghai" , MobileNumber = "23947578593" , Age = "23")'''

#------------#------------#------------#------------#------------#------------#------------
#without using kwargs(keyword arguements)

def StudentInfo(name,City,MobileNumber,Age):
    print("name",name)
    print("City",City)
    print("MobileNumber",MobileNumber)
    print("Age",Age)
StudentInfo(name = "Kapil" , City = "Bawal" , MobileNumber = "9996547555" , Age = "18")
StudentInfo(name = "William" , City = "London" , MobileNumber = "5484946871" , Age = "28")
StudentInfo(name = "John" , City = "Los Angeles" , MobileNumber = "5789498197" , Age = "21")
StudentInfo(name = "Li Zhang" , City = "Shanghai" , MobileNumber = "23947578593" , Age = "23")
    