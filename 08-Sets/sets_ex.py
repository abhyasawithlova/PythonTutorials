s1 = {1, 2, "Python", 3.4}
print(type(s1))
print(*s1)
# Unordered (order is no gaurantee), Mutable, wont allow duplicate values.
print("*" * 10 + " Adding element to Set. " + "*" * 10)
s1.add(5)
print(*s1)
print("*" * 10 + " After adding duplicate element to Set. " + "*" * 10)
s1.add(5)
print(*s1)

print("*" * 10 + " Length of the Set. " + "*" * 10)
print(len(s1))

print("*" * 10 + " Set methods " + "*" * 10)
s2 = {1, 2, 3, 4, 5, 9}
s3 = {3, 4, 5, 6, 7}
diff_s = s2.difference(s3)
print(*diff_s)

s2.difference_update(s3)
print(*s2)
