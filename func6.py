def add(a,b,*c,d,e):
    r=a+b+sum(c)+d+e
    return r
res=add(10,20,30,40,d=50,e=60)
print(res)
