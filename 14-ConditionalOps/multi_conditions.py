#if <condition> <logicalOperator> <condition> <logicalOper> <condition>:
name = "Rama"
age = 62
gender = "male"

# if age > 60 and gender is male, print senior men
# if age > 60 and gender is female, print senior women

if age > 60 and gender == "male":
    print("Senior Men")
elif age > 60 and gender == "female":
    print("Senior Women")

# if number is between 1-100, print number is between 1-100 bucket.
n = 34

if n > 1 and n < 100:
    print("in  1-100 bucket")

# if a number is divsible by 2 or 5 print the number.

n2 = 10
if n2 % 2 == 0 or n2%5 == 0:
    print(f"{n2} is divisible by 2 & 5")

b = True
if not b:
    print("False")
else:
    print("True")



if n.__le__(35):
    print("ljljljlk") 




