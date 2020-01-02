item=['item1','item2','item3','item4','item5',6,7,8,9,10,11,12]
print(item)
# for items in item:
#     print(items)
for i in range(len(item)):
    print(item[i])
# Negative indexing..
print(item[-1])

#Add an item in the last of the list
item.append('LastItem')
print(item)

#Add item in a specific location
item.insert(5,'Item6')
item.insert(-3,'item-3')
print(item)
print(item[-3])

# Remove items from the list
item.remove('item5')
print(item)
i=-2
item.remove(item[i])
print(item)

num=[8,9,6,4,0,2,9,44]
# Sorting the list
num.sort()
#num.reverse()   #it will make the list decending order
print(num)
name=['ram','sam','jodu','modhu','gopal']
name.sort()
print(name)
name_withNumber=['8ram','1sam','7jodu','2modhu','6gopal']
name_withNumber.sort()
print(name_withNumber)

# Reversing a list
name.reverse()
print(name)
print(name.reverse())

# join a list (i.e: Make all the items of a list in a string)
allNames= (', ').join(name)
print(name)
print(allNames)

# Split a string and make the crunch of the string as items of a list
newNames=allNames.split(', ')
print(newNames)

