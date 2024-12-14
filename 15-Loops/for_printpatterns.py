"""
Pattern 1:
1
2 2
3 3 3
4 4 4 4
"""
print("Pattern 1....")
for i in range(1, 5): # 1, 2, 3, 4
    for j in range(i): # r(4)=0,1,2,3
        print(i, end=" ")
    print("\n")

# Excercise : 1
"""
Pattern 2:
*
**
***
****
"""
print("Pattern 2..")
n = 5
for i in range(1, n + 1):
    print("*" * i)

#Excersise: 2
"""
Pattern 3: 
***** 5
**** 4
*** 3
** 2
* 1
"""
print("Pattern 3...")
n = 5
for i in range(n, 0, -1):
    print("*" * i) 
#for i in range(n, 0, -1):  #[5, 4, 3, 2, 1]
#    for j in range(0, i): #i = 3, [0, 1, 2]
#        print("*", end="")
#    print("")

"""
Pattern 4....
A
BB
CCC
DDDD
EEEEE
"""
print("Pattern 4...")
a = 65 # ASCII 65 = A
n = 5
for i in range(0, n): #[0, 1, 2, 3, 4]
    print(chr(a + i) * (i + 1))

"""
Pattern 5:
A
AB
ABC
ABCD
ABCDE
"""
print("Pattern 5....")
a = 65 # A
n = 5
for i in range(0, n): #[0, 1, 2, 3, 4]
    for j in range(0, i + 1): #range(0,1) [0]
        print(chr(a + j), end="")
    print("")

"""
Pattern 6:
AAAAA
BBBB
CCC
DD
E
"""
"""
Pattern 7:
ABCDE
ABCD
ABC
AB
A
"""

"""
Pattern 8:
     *
    * *
   * * *
  * * * *
* * * * * *
"""
print("Pattern 8...")
n = 5
for i in range(0, n): # [0, 1, 2, 3, 4] i = 0
    for j in range(i, n): # range(0, 5) [0, 1, 2, 3, 4]
        print(" ", end="")

    for k in range(0, i + 1):
        print("*", end=" ")
    print("")


