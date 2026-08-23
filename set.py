A = {10, 2, 30, 40,4,80}
B = {100, 30, 80, 40, 60}
print(A)
print(B)
print ("A-B",A.difference(B))
print("Intersection",A.intersection(B))
print("Disjoint: ",A.isdisjoint(B))
print("Subset",A.issubset(B))
print("Superset:", A.issuperset(B))
print("Union:", A.union(B))
A.add('f')
A.discard('f')
A.remove(4)
print('Popped element', B.pop())
B.clear()
print('Set after clearing :',B)
A = B.copy() 

