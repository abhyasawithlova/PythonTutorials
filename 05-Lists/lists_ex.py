l1 = [1,2,3,4, "python", [2.3, 4.5]]
print(type(l1))
print(l1) # prints elements enclosed with square brackets
print(*l1) # prints only elements

# Repeated list , ex. [2, 2, 2, 2, 2]
l2 = ["Python"] * 5
print(l2)

print("*" * 10 + " List methods " + "*" * 10)
# length of the list
print(len(l1))

# list are mutable, means we can append/insert an element to the list.
l1.append("PyList")
print(l1)
l1.remove("python")
print(l1)

# Extend method
print("*" * 10 + " Extend method of list " + "*" * 10)
l3 = [4, 5, 6]
l1.extend(l3)
print(l1)

# Inserting new element at 1st index
l1.insert(1, 22)
print(l1)

# pop the element from list
print("*" * 10 + " Pop method of list " + "*" * 10)
popped_ele = l1.pop(6)
print(popped_ele)
print(l1)

l1[0] = 1.1
print(l1)

l1_sublist = l1[1:5]
print(type(l1_sublist))

print("*" * 10 + " Copy method of list " + "*" * 10)
cl = l1.copy()
print(cl)

print("*" * 10 + " Sort method of list " + "*" * 10)
int_list = [1, 4, 6, 3, 5, 9, 2.5] # 1 < "Py"
int_list.sort()
print(int_list)
















