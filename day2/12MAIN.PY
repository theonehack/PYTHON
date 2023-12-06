import time

h = int(time.strftime("%H"))
m = int(time.strftime("%M"))
s = int(time.strftime("%S"))
print(h, m, s)

if h >= 4 and h < 12:
  print("Good morning sir!")
elif h == 12:
  print("Good noon sir!")
elif h > 12 and h <= 17:
  print("Good afternoon sir!")
elif h > 17 and h <= 21:
  print("Good evening sir!")
else:
  print("Good night sir!")
  
   

