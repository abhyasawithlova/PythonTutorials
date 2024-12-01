d1 = {"name": "Durga", "age": 35, "weight": 65.45}
print(type(d1))
print(len(d1))
d2 = dict({"name": "Durga", "age": 34})
print(type(d2))

# Accessign elements in dictionary.
print(d1)
print(d1["name"])
#print(d1["firstName"])  # key error, since key is not present dict
print("*" * 10 + " Access/Insert keys using [] brackets. " + "*" * 10)
d1["name"]="Padala"
print(d1)

d1["address"]="Bangalore"
print(d1)
# SetDefault and get method.
print("*" * 10 + " Accessing elements using set/get methods. " + "*" * 10)
r = d1.setdefault("address", "AndraPradesh")
print("r=" + r)

r2 = d1.setdefault("phone", "8123717649")
print(d1)
print("r2=" + r2)

g1 = d1.get("address", None)
print("g1=" + g1)

g2 = d1.get("firstName", None)
print("g2=" + str(g2))

print("*" * 10 + " To check key is present or not using in built in method. " + "*" * 10)
print("age" in d1)
print("firstName" in d1)

ks = d1.keys()
print(type(ks))
print(ks)
vs = d1.values()
print(vs)

d1[None] = "None"

print(d1)















