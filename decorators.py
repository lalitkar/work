def add1(a,b):
    print('result is')
    print(a+b+a)
    print('end of result')
def sub1(a,b):
    print('result is:')
    print(a-b)
    print('end of result')
add1(10,20)
sub1(10,20)
def mydec(func):
    def decorated_func(*x,**y):
        print('result is')
        func(*x,**y)
        print('end of result')
    return decorated_func
@mydec
def add2(a,b,c,d):
    print(a+b+c+d)
add2(10,20,30,40)