#update funtion
s={1,2,3}
l={1,3,5,7}
s.update(l)
print(s)


#discard function
s={1,2,3,4,5,6,7,8,9}
s.discard(5)
print(s)


#remove function
s={1,2,3,4,5,6,7,8,9}
s.remove(3)
print(s)

#add function
s={1,2,3}
s.add(9)
print(s)

#pop
s={1,2,3,4}
s.pop()
print(s)

#clear
s={1,2,3,4}
s.clear()
print(s)

#issubset and issuperset
s1={1,2,3,4}
s2={1,2}
o=s1.issuperset(s2)
o1=s2.issubset(s1)
print(o,o1)

#intersection
s={1,2,3}
l={1,3,5,7}
o=s.intersection(l)
print(o)
