l=[100,200,300,400]

r1=map(lambda i:i-10,l)
print(list(r1))

r2=filter(lambda j:j>100,l)
print(list(r2))
import functools as fc

r3=fc.reduce(lambda p,q:p+q,l)
print(r3)
l=[(lambda i:i*i)(a) for a in range(10)]
print(l)


