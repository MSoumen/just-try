a=10
def update():
    global a
    print(id(a))
    a=8
    print(id(a))
    print(a)


print(id(a))
update()
print(id(a))
print(a)
