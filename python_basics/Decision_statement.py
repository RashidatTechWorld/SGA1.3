#trying decision making statement on python
#if the number is positive, we print the approprite message
from re import A

#if, elif, else operators
num = -1000
if num >= 0:
    print(num, "is a Positive")
elif num ==0:
    print(num, "is a zero")
else:
    print(num, "is a negative")
#assignment operators
a = 8
b = 5
c = 10
d = a+b
c-=a
print(c)
d+=c
print(d)
#comparison operators
print(a==b)
print(a!=c)
print(a<<b)
print(a>>b)
#control flow
a = 3
if a >= 0:
    print(a,"is a positive number.")
    print("I am super right.")
