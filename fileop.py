f1=open('out1.txt','w')
x=10
s='python\n'
x=str(x)+'\n'
f1.write(x)
f1.write(s)
f1.flush()
l=[x,s]
f1.writelines(l)
f1.close()
f2=open('out1.txt','r')
r1=f2.read()
print('r1= ',r1)
f2.seek(0)
r2=f2.read()
print('r2=',r2)
f2.seek(0)
while True:
    line=f2.readline()
    if line=='':
        break
    else:
        print(line)
f2.seek(0)
r4=f2.readlines()
print('r4=',r4)
r5=[]
for l in r4:
    l=l.strip()
    r5.append(l)
print('r5=',r5)
f2.seek(0)
for x in f2:
    print('line=',x)
f2.seek(0)
r6=list(f2)
print(r6)
f2.seek(0)
d2=dict(enumerate(f2))
print(d2)
f2.close()
f3=open('out1.txt','a')
f4=open('out2.csv','a')
