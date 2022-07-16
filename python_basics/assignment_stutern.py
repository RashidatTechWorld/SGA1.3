#find the exponentiation of a number
print('Find the exponentiation of a number')

#assigning intergers to variable
x = int(input("Enter number:"))
y = int(input("Enter number:"))

#check if power is 0
if y == 0:
    print(1)

    #if otherwise, perform exponentiation
else:
    x = x**y
    print(x)