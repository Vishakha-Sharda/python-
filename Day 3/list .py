from re import L


L = ["a","b","c"]
print(L)

#insert :to insert a list item at specific index
thislist = ["a", "b", "c"]
thislist.insert(1, "v")
print(thislist)

#append list:to add element.
L = ["a", "b", "c"]
L.append("d")
print(L)


#extend:to append the elements of one list to another
thislist = ["a", "b", "c"]
tropical = ["x", "y", "z"]
thislist.extend(tropical)
print(thislist)