def search(l, in_val):
    if in_val in l:
        return 'id found,id='+str(in_val)+'index='+str(l.index(in_val))
    elif in_val>max(l):
        return 'not found'
    else:
        for i in l:
            if i>in_val:
                return 'val='+str(i)+'index='+str(l.index(i))
def main():
    list1 = [1, 3, 5, 16, 8]
    list2 = [6, 5, 9, 4, 13, 12]
    s = set(list1 + list2)
    l = list(s)
    print(l)
    while True:
        id=input('enter the id')
        id=eval(id)
        se=search(l,id)
        print(se)
        ch=input('quit(y/n)')
        if ch=='y':
            break
if __name__=='__main__':
    main()
