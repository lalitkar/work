t1=(10,20,30)
t2=(i for i in range(10))
print('t1=',t1)
print('t2=',t2)
print('list(t2)=',list(t2))
l=[1,2,3,4]
def squares(m):
    res=[]
    for j in m:
        r=j*j
        res.append(r)
    return res
r1=squares(l)
for a in r1:
    print('a=',a)
def gen_sqr(n):
    for k in n:
        yield k*k
    for l in n:
        yield l*5
r2=gen_sqr(l)
for b in r2:
    print('b= ',b)
print('r2=',list(r2))