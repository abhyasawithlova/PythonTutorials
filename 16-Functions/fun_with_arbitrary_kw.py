# Function with Arbitrary keyword, it takes multiple arguement while calling
# and converts them into list.

def numbers(*argv):
    print(type(argv))
    for i in argv:
        print(i)

numbers(1, 2, 3, 4, 5, 6)