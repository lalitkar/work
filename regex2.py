s='abc123xyz56ABC'
r1=s.split('123')
print(r1)
import re
r2=re.split('\d{3}',s)
print(r2)
r3=s.find('123')
if r3!=-1:
    print('substring found')
r4=re.search('\d{2}',s)
if r4!=None:
    print('digit found')
f=open(r'C:\Users\lab365\Desktop\python\log\serverlog.txt.txt')
data=f.read()
ips=re.findall('\d{3}.\d{3}.\d{3}.\d{3}',data)
print(ips)