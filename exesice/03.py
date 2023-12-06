#making kbc game yoooooo
k=[]
q1=("what is python ??    \n  1--- programing language :             2--- snake  :   \n  3--- bird  :                           4--- animal  :"   )
print(q1)
a=(int(input("in which opposition you want to lock  : ")))
if (a==1):
    print("sat carooooddddddddddd")
    k.append(7)
else:
    print("sorry you lose :")
    k.append(0)


q2=("what is java ??    \n  1--- programing language :             2--- a name   :   \n  3--- list   :                          4--- frog   :"   )
print(q2)
a=(int(input("in which opposition you want to lock  : ")))
if (a==1):
    print("sat carooooddddddddddd")
    k.append(7)
else:
    print("sorry you lose :")
    k.append(0)

d=int(k[0]+k[1])
print("your total ammount is ",d)
