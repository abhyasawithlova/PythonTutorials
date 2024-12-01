# Numeric types
# int, float -- Number data type.

num1 = 10
num2 = 20

print(type(num1))
print(type(num2))

# What operations we can perform on number data types?
# Arithmatic Operations:
# Sum, Subtraction, Multiplication, Division, Exponential, Modulation, Floor division, Ceil division.

sum_of_num1and2 = num1 + num2
print("Type and sum of two variable num1 and num2.")
print(type(sum_of_num1and2))
print(sum_of_num1and2)

print("Type and Division of two variable num1 and num2.")
div_of_num1andnum2 = num1/num2
print(type(div_of_num1andnum2))

length = 10.0
width = 20.5

# Arithmatic Operations: 
# Sum, Subtraction, Multiplication, Division, Exponential, Modulation, Floor division, Ceil division.

sum_of_length_width = length + width

# What is the output data type if we sum Int and Float variable.

print("Type and Sum of Int and Length data types.")
sum_num1_and_length = num1 + length
print(type(sum_num1_and_length))  # float

print("Type and Div of Int and Length data types.")
div_num1_and_length = num1/length  #10/10.0 = 1.0
print(type(div_num1_and_length))
print(div_num1_and_length)

print("Modulation operations between ints")
print(num1 % num2) # 10
print(num2 % num1) # 0
































#my_list = [1, 3, 5, 7, 9, "Hello"]

#print(my_list)
#m_set = {1, 3, 5, 7}
#m_set.add(9)
#print(m_set)
#f_set = frozenset([3, 5, 7, 3])
#print(f_set)

#b_array = bytearray(b"Hello")
#print(b_array)