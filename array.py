import array

nums=array.array('I',[10,20,20,30,40])
print(nums)
# Adding value in array
nums.append(50)
print(nums)
# Reverse the values of array
nums.reverse()
nums.reverse()
print(nums)
# See the address and the size of array
print(nums.buffer_info())
#  COPY The type of nums array into new_array
new_array=array.array(nums.typecode,[100,200,300,400])
print(new_array)
print()

# printing the values of array single
for value in nums:
    print(value,' ',end='')
print()
# Receiving inputs from user
char=array.array('u',[])
count=int(input('How many Characters u want to enter : '))
for i in range(count):
    n=input(' Enter a Character: ')[0]
    char.append(n)
print('Your array is ',char)
print('Address andn Size of your array are ',char.buffer_info())
print()
print('\nBye\n')

