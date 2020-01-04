# No arguments,No return
def func1():
    print('Hello There,')
    print('Good Evening Everybody')
    print()

# No arguments, High returns
def func2():
    print()
    a=int(input('Enter a number: '))
    b=int(input('Enter another number: '))
    c=a+b
    return c

# Take Arguments, No returns
def func3(a,b,c):
    print()
    d=a+b+c
    print('d=',d)

# Take arguments, Give returns
def func4(a,b,c,d):
    print()
    sum=a+b+c+d
    sub=a-b-c-d
    return (sum,sub)
    
# Body of program---
func1()
c=func2()
print(c)
func3(10,20,30)
sum,sub=func4(40,30,20,10)
print('Sum=',sum,'sub=',sub)

