list_of_roll=[1,2,3,4,5,6,7,1,3,5,10,8,9,10,20,30] #list with multiple rollno
set_of_names={'Arun','Barun','Kiranmala','Tarun','Arun','Kiranmala','Tarun'} #set with duplicate names
print(set_of_names)
 # in a class name will same but roll no will unique for everyone so we have to convert set to list and vice versa
 #Set to List
list_of_names = list(set_of_names)
print('-->')
print(list_of_names)
print()
# List to Set
print(list_of_roll)
set_of_roll=set(list_of_roll)
print('-->')
print(set_of_roll)
print('\n\n')

# Some set operations
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1)
print(set2)

# Union
setU=set1.union(set2) #set1|set2
print(setU)

# Intersection
setI=set1.intersection(set2) #set1 & set2
print(setI)

# Difference
setD=set1.difference(set2) #set1-set2
print(setD)

#checking
if set1==set2:
    print('Set1 is equal to Set2')
if set1>set2:
    print('Set2 is proper subset of Set1')
if set1!=set2:
    print('Set1 is nott equal to Set2')

# make the set NULL set
set1.clear()
set2.clear()
print(set1)
print(set2)
