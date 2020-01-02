# Mutable = Changable ex:Lists,dictionary,sortedDictionary
# Immutable = Unchangeble ex:tuple
aList=[1,2,3,4,5,6]
aTuple=(1,2,3,4,5,6)
print(aList)
print(aTuple)

#Check mutabilty in tuple
print(aTuple[3])
# aTuple[3]=30  #Tuple is Immutable...Proved

#Check mutabilty in tuple
print(aList)
aList[3]=30
print(aList)  #List is Mutable .. Proved

aTuple_with_list=(1,2,3,4,5,[0,0,0,0,0,55])
print(aTuple_with_list)
aTuple_with_list[-1][-1]=0
print(aTuple_with_list)
