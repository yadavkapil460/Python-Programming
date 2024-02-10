def exception(x,y):
  try :
     result = x/y
     print("Yiour Division is : ",result)
  except ZeroDivisionError:
      print("You Can't divide by 0")

exception(10,5)
exception(5,0)
