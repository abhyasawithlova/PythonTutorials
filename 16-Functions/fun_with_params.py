# Function with arguements.

"""
def <functionname>([arguements]):
    # your code.
"""
print("Function with params demo")

def greet(name):
    print(f"Hello {name}, how are you.")

greet("Ramya")

# Function with multiple positional arguements.
def biodata(name, age, address):
    greet(name)
    print(f"Hello you are {name}, and {age} year old, and came from {address}")
    biodata(name, age, address)

biodata("Ramya", 23, "AndraPradesh")
#biodata(address="AndhraPradesh", name="Ramya", age=23)


