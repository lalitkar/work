def add(g):
    a=g
    b=30
    c=a+b
    print(c)
add(10)

def get_ips():
    f=open('C:\Users\lab365\Desktop\python\log\serverlog.txt.txt')
    ips=[line.split()[6].lstrip('/pics') if 'pics' in line.split()[6] else 'no image' for line in f2 if line[:3].isdigit()]
    print(ips)

get_ips()