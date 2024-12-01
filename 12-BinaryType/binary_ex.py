by = b"I am learning python"
print(type(by))
print(*by)

by2 = bytearray("Hellow World", "utf-8")
print(*by2)

print(by2.decode("utf-8")) # ByteArray to String.

s = "Hello Python"
bs = s.encode("utf-8") # String to ByteArray
print(type(bs))

bj=b"".join([bytearray(b'Hello'), bytearray(b' World')])
print(type(bj))
print(*bj)
print(bj.decode("utf-8"))


