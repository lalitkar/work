list1=[1,3,5,16,8]
list2=[6,5,9,4,13,12]
s=set(list1+list2)
l=list(s)
print(l)
def search(a):
    if a in l:
        print('number is:',a,'index is:',l.index(a))
    else:
        for j in l:
            if j>int(a):
                print('number is:',j,'index is:',l.index(j))
                break
        else:
            print('not found')
b=int(input('enter the id'))
search(b)






