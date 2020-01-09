def add(a,b):
    return a+b
i=add(10,20)
print(i)
def get_ips(file_path,mode):
    f=open(file_path)
    if file_path.endswith('.txt'):
        ips=[line.split(',')[0] for line in f]
        return ips
    else:
        ips=[line.split()[0] for line in f]
        return ips
r1=get_ips('log_report.txt','r')
print(r1)