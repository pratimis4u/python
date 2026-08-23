s =input("Enter string")
l = []
le = len(s)
for i in range (0,le):
	l.append(s[i])
for i in range(0,le):
	for j in range(0,le):
		if l[i]<l[j]:
			l[i],l[j]=l[j],l[i]
s2=""
for i in range(0,le):
	s2 = s2+l[i]

print(s2)
