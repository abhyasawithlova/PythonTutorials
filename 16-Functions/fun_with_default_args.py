# Function with default arguement, 
# and default value will be used when no arguement passed while caling.

def greet(name="User"):
    print(f"Hello {name}")

greet() # No arguement, hence name is User.
greet("Ramya") # default value for name is replaced with Ramya.

