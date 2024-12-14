#while(condition):
    # code

#while(True):  -- infinite loop
#    print("Hello")
# Print number upto 10
flag = True
i = 0
while (flag):
    i+=1 # i = i + 1
    print(i)
    if i >= 10:
        flag = False
print("I am done")


print(10 * "*" + "Welcome to Calculator world" + 10 * "*")
print("Hello, Enter two numbers:")
n1 = int(input("1st Number:\n"))
n2 = int(input("2nd Number:\n"))
print("Thats great, choose arithmatic operations from the list below:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quit")
cont = True
while(cont):
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
    elif sel_op == "5":
        cont = False
    else: 
        print("Invlaid selection.")
    print("Result is " + str(result))
