import array as arr

a1 = arr.array('i', [1, 3, 4, 2, 5, 9, 10, 6, 8, 7])
print(*a1)
print(len(a1))

# find an element 9.
k = 9
found = False # This flag used to determine whether we found element or not in an array.
for i in range(0, len(a1)):
    print(f"Iteration: {i}")
    if a1[i] == k:
        print(f"Found the element at index {i}")        
        found = True
        break

if not found:
    print("Element doesn't exist in Array.")

# Worst case: O(N), N is length of the array.
# Best case: O(1), found the element in first index.
# Average case: O(N/2), found the element in middle.
