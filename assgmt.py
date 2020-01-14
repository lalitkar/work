'''this is procedure-oriented progrom
    to search a list for ids'''
list1=[1,3,5,16,8]
list2=[6,5,9,4,13,12]
s=set(list1+list2)
l=list(s)
print(l)
while True:
    in_val=input('enter the id')
    in_val=int(in_val)
    if in_val in l:
        print('device id found,id=',in_val,'its index:',l.index(in_val))
    elif in_val>max(l):
        print('not found')
    else:
        for i in l:
            if i>in_val:
                print('val=',i,'index=',l.index(i))
                break
    ch=input('do you want yo quit (y/n):')
    if ch=='y':
        break