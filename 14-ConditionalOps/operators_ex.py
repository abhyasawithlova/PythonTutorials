# it provides efficient functions equivalent to intrinsic operations
# example: add two number, res = a + b, a - b , a * b
# operator.add(a, b) - returns sum of a, b.
import operator as op

print(op.add(55, 44))
print(op.abs(-4.3325))
print(op.concat("Hello", " World"))
print(op.contains("Hello", "H"))
print(op.contains([1, 3, 5, 7], 5))

#Logical Operations in Operator module
print(10 * "*" + "Logical Operations" + 10 * "*")
b = op.eq("Hello", "hello")
print("b->" + str(b))

op.ge(3, 4)