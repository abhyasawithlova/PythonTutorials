# Strings
## str() represents the type string in python.
## String is a sequence of immutable unicode characters.
## Ex. "Hello", "Python"
# '', "", '''...''', """...."""

s1 = "Hello"
#product_description = "sfdsfdsfdsgdsgdsgdsggsdfsfgdsgdsfgdsgsdfdsfdsfdsfdsfd
#sfdsfdsfdsfdsgsdfdsgsgdfsgdfsgdfsgdfgfsgdsgfsdgfsgfsgdfsgdfsgdfgfdsdfsgdfgdfsgdsgdfgdgdgd"
str()

product_description = """sfdsfdsfdsgdsgdsgdsggsdfsfgdsgdsfgdsgsdfdsfdsfdsfdsfd
sfdsfdsfdsfdsgsdfdsgsgdfsgdfsgdfsgdfgfsgdsgfsdgfsgfsgdfsgdfsgdfgfdsdfsgdfgdfsgdsgdfgdgdgd"""

print(s1)

# Immutability
i1 = "Hello"
print(id(i1))

i1 = i1 + ", World"
print(id(i1))

# String index and slicing
print(10 * "*" + " Indexing and slicing " + 10 * "*")
s_1 = "Python"
  #print(s_1[6]) # IndexError
print(s_1[0]+s_1[1])
print(s_1[0:1]) #right side of the colon is Exclusive. 0 and <1
print(s_1[0:2]) # 0<i<2 

print(s_1[2:]) # prints from 2 index char to end of the string.
print(s_1[:5])

print(s_1[-1])

# String object methods
print(10 * "*" + " Object methods " + 10 * "*")
s_method = "i Am Learning Python"
print(s_method.capitalize())
print(s_method.casefold())
p = "Hello"
print(p.casefold() == "hello")

print(s_method.casefold().endswith("python"))

# Strings concatenation and repetition
print(10 * "*" + " Concatenation and repetition " + 10 * "*")
c = "I am " + "Learning " + "Python"
print(c)

print(5 * " * ")

# String formatting and escaping
print(10 * "*" + " Formatting and Escaping " + 10 * "*")
fs = "\'\tHello, world\""  # "Hello, World" forward slash used for escaping. \', \", \t,\n
print(fs)
py = "Python"
fs1 = f"I am learning {py}"
print(fs1)
print("IndexVars: I am learning {}, from last {} week".format(py, 1))
print("NamedVars: I am learning {py}, from last {duration} week".format(duration=1, py=py))
print(f"I am learning {py}")

# String built in operations
print(10 * "*" + " Build In Operations " + 10 * "*")
name = "durga"  # 100 117 114 103 97
print("Length of name: " + str(len(name)))
print("Min of name: " + min(name)) # Returns min value char as per ASCII table.
print("Max of name: " + max(name)) # Returns max value char as per ASCII table.
print("Ord of name: " + str(ord("A"))) # Ord method returns ASCII number of the string character.
print("Chr of 67 :" + chr(111)) # Chr method returns Un-code (ASCII) String for the number.
# Print or define raw strings.
print(10 * "*" + " Raw Strings " + 10 * "*")
# r prefix to the string makes it as raw string, and ignores escape characters.
path = r"C:\t\/Users/durgalovababupadala/AbhyasaWithLova/PythonPractice/03-Datatypes/string_type.py"
print(path)

s = "I am Practicing Python"
# using slice substring Practicing word
i = s.find("Practicing") #which index Practicing word starts
e = i + len("Practicing")  #Which index Practicing word ends.

print("Sliced string is: " + s[i:e])





