import assgmt_func as af
while True:
    l=[10,20,30,40]
    i=input('enter the id')
    i=eval(i)
    r=af.search(l,i)
    print(r)
    ch=input('quit y/n')
    if ch=='y':
        break
