#Break: Loop control statement, to exit from the current iteration.
# I have list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], find a first number which can be divisible by 2, 3
print("*" * 10 + "Break....")
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in l1:
    print(f"is {i} divisible by 2 & 3")
    if i % 2 == 0 and i % 3 == 0:
        print(f"Hurray we found it, it is {i}")
        break

# Continue: Is a loop control statement, it force to the next iteration.
# I have a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], I want to print double the value of event numbers.
## 2 = 2 * 2
## 3 = continue to next iteration.
print("*" * 10 + "Continue....")
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in l2:
    if i % 2 != 0:
        print(f"Found Odd number, hence continue{i}")
        continue
    print(f"Double the value of {i} is {i * i}")

#Pass: It does nothing, used as place holder to statement/code to avoid python compilation errors.

def hello():
    pass

print(hello())
