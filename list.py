l1=list()
for i in range(3):
    l1.append(input("Enter in list: "))
print("length=",len(l1))
l1.insert(1,input("Enter in list: "))
l2=[1,23,"hii"]
l1.extend(l2)
print("extending: ",l1)
l3=[2,1,0,5,4]
print(l3)
print("Count=",l3.count(43))
print("Sum=",sum(l3))
print("Index of 2",l3.index(2))
print("Min=",min(l3))
print("Max=",max(l3))
l3.sort()
l3.reverse()
print("Popped Element: ",l3.pop())
print(l3)
del l3[0]
l3.remove(2)
l2=l1.copy()
l1.clear()