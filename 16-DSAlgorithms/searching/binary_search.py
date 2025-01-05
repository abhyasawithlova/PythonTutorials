import array as arr

a1 = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(*a1)
print(len(a1))

l = 0
r = len(a1) - 1 # last index of the array.
m = 0

k = 13 # desired element
found = False

i = 0
while l <= r:
    print(f"Iterations:{i}")
    i+=1

    # find the mid element.
    m = (l + r) // 2
    print(f"Mid index: {m}")
    # check if k equals to the mid element, then return no more comparisons.
    if a1[m] == k:
        print(f"Found the element at {m}")
        found = True
        break

    # check if k is greater of mid element, then ignore left portion of the array.
    if k > a1[m]:
        l = m + 1
    
    # check if k is less than mid element, then ignore right portion of the array.
    if k < a1[m]:
        r = m - 1


if not found:
    print("Element not found in an array.")
