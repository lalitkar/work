#Strings
a='PERSON'

b="person's"
c='''person height is 21"'''

s1='hello'
s2='py'
s3=s1+s2
s4=s1*10
e='person\'s'
print(e)
f='wel come'
print(f[-4:])
i=10
j=str(i)
k=str('python')

r1=f.startswith('wel')

r2=f.isupper()
r3=f.upper()

l='asd'
r4=l.isalpha()
m='123'
r5=m.isdigit()
n='weyg123'
r6=n.isalnum()

r7=f.count('e')
r8=f.rindex('e')
r9=f.find('e',1,8)

p='  wel cme   '
r10=p.strip()
r11=p.lstrip()
r12=p.rstrip()

q='[wel[come][]'
rs=f.replace('o','a')
print(rs)
ra=f.split()
rw=f.split('e')
print(ra,rw)
rq='add of {} and {} is {}'.format(f[1],f[3],f[5])
print(rq)
