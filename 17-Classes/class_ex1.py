#Simple class called Product

class Product:
    category = "Electronic" # class attribute

    def __init__(self, product_id, product_name , product_price):
        """
        __init__() method is called as initialized (constructor).
        used to initialize instance attributes. (id, name, price are instance attributes)
        """
        # instance attributes
        self.id = product_id
        self.name = product_name
        self.price = product_price

    def display(self):
        """
        Instance method to display produciton information.
        """
        print(5 * "*" + " Product details " + 5 * "*")
        print(f"Product id: {self.id}")
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")

# To access class attributes, we can use class Name directly.
print(f"Product Class Attribute category: {Product.category}")

# To access instance variable, you must create an object to the class (instance)
mobile = Product(product_id=1, product_name="Samsung Mobile", product_price=12000)

print(type(mobile))
print("Mobile Name:", mobile.name)
mobile.display()

