import time
timestamp = time.strftime('%H,%M,%S')
hour = int(time.strftime('%H'))
print(hour)

if 0<hour<12 :
    print("good morning")
    
elif 12<hour<24:
    print("good evening")
    
else :
    print("invalid error")