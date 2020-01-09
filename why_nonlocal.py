
def acc():
    c=0
    def ca():
        nonlocal c
        c=c+1
    def da():
        nonlocal c
        c=c-1
    def ta():
        print('total=',c)
    return ca,da,ta
f1,f2,f3=acc()
f1()
f1()
c=100
f2()
f3()