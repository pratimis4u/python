d1={0:0,1:1,2:2}
print(d1.keys())
print(d1.values())
d4=d1.copy()
d4.clear()
print(d4)
d2=d1.fromkeys(range(3),20)
print("Value of key a is ",d1.get('a'))
print(d2.get(100,"abcd"))
d3={}
d3.update(d2)
d3.pop(0)
print("deleting first element",d3)
print("length=",len(d2))
d2.popitem()
print("deleting last element",d2)


