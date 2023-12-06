#list
mathresult = [3,4,5,"khawar",True ,45,47,78,90]
#different datatype can be added in a list
print(mathresult)
print(type(mathresult))
#slising 
print(mathresult[0:])
print(mathresult[0:3])
print(mathresult[1:-2])
print(mathresult)
print(mathresult[0:9:2])
print(mathresult[0:9:3])
print(mathresult[0:9:4])
print(mathresult[0:9:5])

#posetive index
print(mathresult[0])
print(mathresult[4])
print(mathresult[3])


#negative index 
print(mathresult[-0])
print(mathresult[-1])
print(mathresult[-2])
print(mathresult[-3])


#printing one index in different ways
print(mathresult[-3])
print(mathresult[2])
print(mathresult[5-3])
print(mathresult[len(mathresult)-3])

#cheking somethint is avelable or not in list

if 7 in mathresult:
    print("yes 5 is avelable in list")
else:
    print("no its not avelablein list")

if "khawar" in mathresult:
    print("yes 5 is avelable in list")
else:
    print("no its not avelablein list")    

if "kha" in "khawar":
    print ("yes")  



    
