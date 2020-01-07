a=0
while a<10:
    print('a=',a)
    a=a+1
s='python'
b=0
while b<len(s):
    print(s[b])
    b=b+1
l=['fn','ln','Adr','a1','fn','Adr','a2']
j=0
while j<len(l):
    if not l[j].startswith('a'):
        j=j+1
        continue

    print(l[j])
    j=j+1
    print('last statement of while')
cart=[]
while True:
    i=input('enter item')
    cart.append(i)
    ch=input('continue y/n ?')
    if ch=='n':
        print('cart=',cart)
        break

