#for i in range(10):
#    print("*")

# write 8 table up to 20.
print(10 * "*" + " Table 8 " + 10 * "*")
for i in range(1, 21): # 1 -- 20
    print(f"{i} * 8 = {i * 8}")

print(10 * "*" + " Iterator over Strings " + 10 * "*")
s = "Hello Python" # seq of characters
# Iterate over string, and print only vowels. [a, e, i, o, u]
for ch in s:
    if ch in "aeiou":
       print(ch)
# Iterate over String, and print count of vowel and consonents
s1 = "Hello World"

l = ["Hello", "Python", "World"]
for s in l:
    print(s)

print(10 * "*" + " Inner Loops " + 10 * "*")
for i in range(0, 4): # 0, 1, 2, 3  -- ofl
    for j in range(0, 4): # 0, 1, 2, 3  -- ifl
        print(f" i = {i}, j = {j}")





