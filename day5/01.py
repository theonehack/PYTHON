l=[1,3,5,4,6,8,9]
print(l)
l.reverse()
print(l)
l.append(7)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
print(l.count(1))


m = l
m[1]=2
print(m)

m.insert(0,12)
print(m)
d=[40,50,60]
k=l+d
print(k) 
l.extend(d)

print(l)