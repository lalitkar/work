class account1:
    def adduser(self,n):
        self.name=n
    def viewuser(self):
        return self.name
    bank=1233
    @classmethod
    def bankrules(cls,area):
        return 'bankrules '+area
    @staticmethod
    def bankinfo():
        return 'bank info'
    def __init__(self):
        print('sb logic here')
cust1=account1()
cust2=account1()
cust1.adduser('c1')
cust2.adduser('c2')
print(cust1.bank)
print(cust1.bankrules('blr'))
print(account1.bankinfo())
print(cust1.viewuser())
print(cust2.viewuser())
class account2(account1):
    def addadhar(self,a):
        self.adhar=a
    def viewadhar(self):
        return self.adhar
    def viewuser(self):
        return 'welcome '+self.name
    def __init__(self):
        account1().__init__()
        print('ca logic here')
cust3=account2()
cust3.adduser('c3')
print(cust3.viewuser())
print(account2.bank)
print(account2.bankinfo())
cust3.addadhar('a1')
print(cust3.viewadhar())
class RBI:
    def viewrules(self):
        return 'RBI rules'
class account3(account2,RBI):
    pass
cust4=account3()
print(cust4.viewrules())
class govt:
    def viewrules(self):
        return 'govt rules'
class account4(account3,govt):
    pass
cust5=account4()
print(cust5.viewrules())
print(govt.viewrules(cust5))
class accounts5(account3):
    def __init__(self):
        self.gov=govt()
cust6=accounts5()
print(cust6.viewrules())
print(cust6.gov.viewrules())
class account6():
    def __init__(self,n):
        self.name=n
    def __add__(self, x):
        return self.name+x.name
    def __str__(self):
        return self.name
    def __len__(self):
        return len(self.name)
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        c=self.count
        if c<len(self.name):
            self.count+=1
            return self.name[c]
        else:
            raise StopIteration
cust7=account6('abc')
cust8=account6('xyz')
result=cust7+cust8
print('result =',result)
print('cust7=',cust7)
print('length=',len(cust7))
for i in cust7:
    print('i=',i)
from abc import ABC,abstractmethod
class account(ABC):
    def adduser(self,a):
        self.name=a
    @abstractmethod
    def viewuser(self):
        pass
class myaccount(account):
    def viewuser(self):
        return 'hello '+self.name
b=myaccount()
b.adduser('B')
print(b.viewuser())

#a=account()
