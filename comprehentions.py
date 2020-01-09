l1=[i for i in range(10)]
print(l1)
l2=[i*i for i in l1 if i%2==0]
print(l2)
f=open('out1.txt')
l3=[line.strip() for line in f]
print(l3)
f2=open(r'C:\Users\lab365\Desktop\python\log\serverlog.txt.txt')
ip=[line.split()[0] for line in f2 if line[:3].isdigit()]
print(ip)
f2.seek(0)
ip2=(line.split()[0] for line in f2 if line[:3].isdigit())
print(list(ip2))
f2.seek(0)
im=[line.split()[6].lstrip('/pics') if 'pics' in line.split()[6] else 'no image' for line in f2 if line[:3].isdigit()]
print(im)
hosts=['h1','h2']
ips=['ip1','ip2']
d={k:v for k,v in zip(hosts,ips)}
print(d)