class search():
    def __init__(self,l1,l2):
        r=l1+l2
        r=set(r)
        r=list(r)
        self.l=r
    def search_element(self,in_val):
        if in_val in self.l:
            return 'id found,id=' + str(in_val) + 'index=' + str(self.l.index(in_val))
        elif in_val > max(self.l):
            return 'not found'
        else:
            for i in l:
                if i > in_val:
                    return 'val=' + str(i) + 'index=' + str(self.l.index(i))
def main():
    l1 = [1, 3, 5, 16, 8]
    l2 = [6, 5, 9, 4, 13, 12]
    a=search(l1,l2)
    r=a.search_element(8)
    print('result=',r)
if __name__=='__main__':
        main()


