# Usage of If else else-if

is_cold = True
is_rain = False
#if it is cold carry jacket, else dont carry.
if is_cold:
    print("Hello customer please carry your jacket")
else:
    print("It is going to hot, dont carry jackets to reduce the weight.")

#if it is cold carry jacket, if it is rain carry umbrella, else with fee hands.

if is_cold:
    print("Carry jacket")
elif is_rain:
    print("Carry umberella")
else:
    print("come with free hands")

# Nested Ifs.
print("*" * 10 + "Nested Ifs." + "*" * 10)
# if it is cold and you are above 60 please carry jackets and mufflers
# else free hands
age = 65
if is_cold:
    if age > 60:
        print("carry jackets and muflers")
    else:
        print("only carry jackets")
else:
    print("come with free hands.")
