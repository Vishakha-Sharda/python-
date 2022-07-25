a=10
def f1():
    print('f1',a)
def g():
    a=20
    print('g',a)
def h():
    global a
    a=30
    print('h',a)
    print('glo',a)

f1()
print('glo',a)
g()
print('glo',a)
h()
print('glo',a)