#elif 
a = 33
b = 33
if b < a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  #else
  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#for loop
colours = ["red", "blue", "green"]
for x in colours:
  print(x)

  #break
  fruits = ["litchi", "banana", "berry"]
for x in fruits:
  print(x)
  if x == "litchi":
    break

#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


  #paass 
  a = 33
b = 200

if b > a:
  pass
