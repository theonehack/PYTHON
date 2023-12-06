# strings are immuteble
a="!!!khawar!!!!!"
b="suraj khawar ehesan"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("khawar","suraj"))
print(b.split(" "))
# capitalize 
c="khawar"
print(c.capitalize())
print(c.count(a))

str1="welcome to the console !!!"
print(str1.endswith("to", 4, 10))

str2="he's name is khawar. he is a good boy."
print(str2.find("is"))

str1 = "Welcome to the Console!!!"
print(str1.center(50))

str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))


str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())


str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.islower())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())