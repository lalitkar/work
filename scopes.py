x=10
def f1():
    x=20
    def f2():
        global x
        x=200
        print('f2=',x)
    f2()
    print('f1=',x)
f1()
print('Global=',x)