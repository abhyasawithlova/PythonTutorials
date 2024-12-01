# range using 3 arguements. range(start, stop, step)
r1 = range(0, 10, 1)
print(type(r1))
print(r1)
print(*r1)

# range using 2 arguements, range(start, stop) default step is +1
r2 = range(0, 5) #+1
print(*r2)

# range using single arguement, range(stop) default start is 0, and step is +1
r3 = range(4)
print(*r3)

#In built in method.
print("*" * 10 + " In built in method with range " + "*" * 10)
r4 = range(0, 10, 2)
print(8 in r4)

# Accessing range elements using index.
print("*" * 10 + " Index based access from range and slicing " + "*" * 10)
r5 = range(0, 10, 1)
print(r5[3])

print(*r5[0:3]) # [:4], [3:]

print("*" * 10 + " Negative step in range " + "*" * 10)
r6 = range(10, 0, -1) # 10 9 8 7 6 5 4 3 2 1
print(*r6)
print(r6[-1]) # it returns last index value.

# we shouldn't give zero as step value.
r7 = range(0, 10, 0)

# list(r7)





