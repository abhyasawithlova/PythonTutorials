# Print whether a list contains Even or Odd number of elements.
# i.e. len([1, 2 ,3 ,"abc"]) -> 4, if size is even print("List has even number of elements")

l1 = [1, 2, 3, 4, 5, "abc", 4.5, 5.4]
# get the size and assign to variable called size
size = len(l1)
# check if size is even or odd
if size % 2 == 0:
    print("List contains even number of elements.")
else:
    print("List contains odd number of elements.")

# Design a calculator by capturing input fron terminal (input)

print(10 * "*" + "Welcome to Calculator world" + 10 * "*")
print("Hello, Enter two numbers:")
n1 = int(input("1st Number:\n"))
n2 = int(input("2nd Number:\n"))
print("Thats great, choose arithmatic operations from the list below:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
sel_op = input("Your Selection:")

result = None
if sel_op == "1" or sel_op.casefold() == "one":
    result = n1 + n2
elif sel_op == "2":
    result = n1 - n2
elif sel_op == "3":
    result = n1 * n2
elif sel_op == "4":
    result = n1/n2
else: 
    print("Invlaid selection.")
print("Result is " + str(result))


