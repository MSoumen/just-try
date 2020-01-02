# Loops = while,for

while True:
    print("It's true",'infinite') #infite loop without break
    break

i=1
while i<=10:
    i+=1
    if i==5:
        #continue
        break
    print('i=',i)

print()
# for loop
for i in range(-111,5,20):
    print(i,' ',end='')

print()
print('\n','Good Bye','\n')
