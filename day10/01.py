s1 = {2,6,4,6}
s2 = {1,3,5,6}

#set addition methods
print(s1.union(s2))
#s1.update(s2)
print(s1)


#set intersection 
print(s1.intersection(s2))

#set intersection_update

#s1.intersection_update(s2)
#print(s1)


#symmetric difference
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

#set method it checks that 2 sets are different or not 
cities = {"Tokyo1", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid1"}
print(cities.isdisjoint(cities2))

#The issuperset() method checks if all the items of a particular set are present in the original set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))

#If you want to add a single item to the set use the add() method.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

#If you want to add more than one item,
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

#We can use remove() and discard() methods to remove items form list.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

#The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo2")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
#cities.remove("Tokyo2")
print(cities)

#This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#del is not a method, rather it is a keyword which deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
#del cities
print(cities)

#This method clears all items in the set and prints an empty set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)