import array as arr

def binary_search(a, k) :
    l = 0
    r = len(a) - 1 # last index of the array.
    m = 0

    found = False

    i = 0
    while l <= r:
        print(f"Iterations:{i}")
        i+=1

        # find the mid element.
        m = (l + r) // 2
        #print(f"Mid index: {m}")
        
        # check if k equals to the mid element, then return no more comparisons.
        if a[m] == k:
            print(f"Found the element at {m}")
            found = True
            break

        # check if k is greater of mid element, then ignore left portion of the array.
        if k > a[m]:
            l = m + 1
        
        # check if k is less than mid element, then ignore right portion of the array.
        if k < a[m]:
            r = m - 1
    
    if not found:
        print("Element not found in an array.")


a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

binary_search(a=a, k=12)



