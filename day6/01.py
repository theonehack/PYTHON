countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)





countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


#count() how many number
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

#index() method where is number find 
Tuple2 = (0, 1, 2, 2, 3, 1, 3, 2)
res = Tuple2.index(3)
print('Count of 3 in Tuple1 is:', res)

#slising tuple
res = Tuple2.index(3,4,8)
print(res)