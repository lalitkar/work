f1=open('log_report.txt','w')
f2=open('log_report.csv','w')
f1.write('IP\tDATE\tPICS\tURL')
f2.writelines(['IP,','DATE,','PICS,','URL\n'])
f3=open(r'C:\Users\lab365\Desktop\python\log\serverlog.txt.txt')
for line in f3:
    if line[:3].isdigit():
        sp=line.split()
        ip=sp[0]
        dt=sp[3]
        dt1=dt[1:12]
        dt2=dt[1:dt.index(':')]
        print(ip,dt1)
        if 'pics' in sp[6]:
            im