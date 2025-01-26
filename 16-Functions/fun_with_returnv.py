# Function with return value.
# Syntax
"""
def <functionname>([parameters]) -> return_type:
    #your code
    return <value>
"""

def is_minor(age):
    print("Checking age is under minor group.")
    flag = age < 18
    return flag

f = is_minor(19)
print("Is  minor? ", f)