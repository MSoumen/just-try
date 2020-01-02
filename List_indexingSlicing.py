num=[1,3,2,6,7,2,9,10,15]

#Slice a list into two portion
print(num[:])
print(num[0:3]) # where pattern is list[ inclusive : exclusive ] (i.e: inclusive <= list_item < exclusive)
print(num[2:len(num)])
print(num[-2:])
print(num[-3:-1])
print(num[-5:])

#Reverse the num[-5:]
numRev=num[-5:]
numRev.reverse()
print(numRev)

#Cut the list with some Hopping
print(num[0:len(num):1])
print(num[::1])
print(num[::2])
print(num[::3])
print(num[::4])
print(num[::5])
for i in range(len(num)-1):
    print(num[0:i+1])

windowSize=4
for i in range(len(num)-(windowSize-1)):
    print(num[i:i+windowSize])
