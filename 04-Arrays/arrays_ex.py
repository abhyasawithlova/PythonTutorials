import array as arr

arr1 = arr.array('l', [2, 3])

print(type(arr1))
print(arr1)  # Definition and elements.
print(*arr1) # only elements.

# Is array mutable or immutable? Mutable

arr1.append(4) # [2,3,4]

print("Array after appending 4: ")
print(*arr1)
print(arr1)

arr1.append(2)
arr1.append(2)
print(arr1)

occurance_of_2 = arr1.count(2)  # returns number of occurances of the element.
print(occurance_of_2)

# Length of the array.
print(len(arr1)) # prints number of elements in the array.

print("print.itemsize.")
print(arr1.itemsize)

arr1.remove(2) # it removes first occurance of element.
print(arr1)
arr1.remove(2)
print(arr1)

#arr1.remove(5) # value error.

# arr1.clear() it was added in 3.13

# arr1.append(4.5) it throws Type error.

print("ToList method...")
l = arr1.tolist()
print(type(l))
l.append(4.5)
print(l)
#print(arr1)

