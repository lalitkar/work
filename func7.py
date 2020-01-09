def add(a,b=10,*c,d,e,**f):
    print('total keyword only avg=',f)
    r=a+b+sum(c)+d+e+sum(f.values())
    return r
i=add(10,30,d=20,e=30,f=40,g=50)
print(i)
