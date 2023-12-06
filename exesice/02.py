#exesice 2 good morning sir
import time 
tim=time.strftime('%H:%M:%S')
print(tim)

hour =(int(time.strftime('%H')))
if(hour>=0 and hour<12):
    print("good morning sir")
elif (hour==12):
    print("good noon sir")    
elif (hour>=12 and hour<19):
    print("good afternoon sir")
elif (hour>=19 and hour<24):
    print("good night sir")                  