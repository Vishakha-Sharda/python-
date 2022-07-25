#airthmetic OPERATOR 
x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2
#LOGICAL OPERATOR
x = 5

print(not(x > 3 and x < 10))

# bitwise operators

a = 10
b = 4

#  bitwise AND operation
print("a & b =", a & b)

#  bitwise OR operation
print("a | b =", a | b)

#  bitwise NOT operation
print("~a =", ~a)

#  bitwise XOR operation
print("a ^ b =", a ^ b)

#assignment operator
x = 5

x += 3

print(x)

#relational operator
x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3

#identity operator
x = ["a", "b"]
y = ["a", "b"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#membership operator
x = ["Punjab", "ludhiana"]

print("ludhiana" in x)

