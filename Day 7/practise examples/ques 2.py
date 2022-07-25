l= [1,2,3,0,1,1,4,5,2,3] 
print ("The list is: " + str(l)) 
result = [] 
for i in l: 
    if i not in result: 
        result.append(i)
print ("The list after removing duplicates : " + str(result))