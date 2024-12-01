t1 = (1, 2, (3, 4), "Python", 5.6)
print(t1)
print(*t1)
print(len(t1))
print(t1[2])

# Ways to create tuple in python.

#Using brackets
#t1 = (1,2 , "Hi")

#Without brackets
t2 = 1, 2, "Hi"
print(type(t2))

#tuple constructor
t3 = tuple([1, 2, "Hi"])
print(type(t3))

#Repeated elements in tupple
print("*" * 10 + " Repeated elements in tuple " + "*" * 10)
t4 = (4,) * 5
print(t4)
print(type(t4))


print("*" * 10 + " Slicing in tuple " + "*" * 10)
t1_slice = t1[0:3]
print(type(t1_slice))
print(t1_slice)

# Empty tuple
t_empty = ()

# Tuple is Immutable
print("*" * 10 + " Immutable tuple " + "*" * 10)
#t1[0]=1.1

print("*" * 10 + " Nested tuple " + "*" * 10)
t5 = ((1, 2, 3), (4, 5, 6))
print(type(t5))
print("*" * 10 + " Index method in tuple " + "*" * 10)
t1_indx = t1.index((3, 4), 1, len(t1)) # 1arg: value, 2nd: from which index it has start searching, 3rd: till which index it has to search.
print(t1_indx)

print(t1[2])






