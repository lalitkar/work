s='python'
for a in s:
    print('a=',a)
b='java'
l=[10,20,30]
for b in l:
    print('b=',b)
d={'z':10,'y':20}
for k in d.keys():
    print('keys=',k,'values=',d[k])
for i in d.items():
    print('i=',i[0],i[1])
host=['h1','h2','h3']
ips=['ip1','ip2']
z=zip(host,ips)
print(list(z))
for h,p in zip(host,ips):
    print(h,p)
r1=range(10)
r2=range(1,10)
r3=range(1,10,2)
print(list(r1),list(r2),list(r3),sep='\n')
for i in range(0,len(host)):
    print(host[i])
comp=['ibm','del1','sap','del2']
for i in comp:
    if i.startswith('del'):
        print('found')
        break
else:
    print('nf')
for i in comp:
    if not i.startswith('del'):
        continue
    if i.startswith('del'):
        print('some logic')
    print('last line of for')