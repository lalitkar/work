def add(a,b=10,*c):
    print('variable=',c)
    r=a+b+sum(c)
    return r
k=add(10,20,30,40,50,60)
print(k)

def telnet(host=None,port=None,*cmds):
    import subprocess
    result=[]
    for each_cmd in cmds:
        r=subprocess.check_output(each_cmd,shell=True)
        result.append(r)
    return result
r=telnet(0,0,'dir','type log_report.csv')
print('r=',r)
f=open('cmd_out.txt','w')
r=[line.decode() for line in r]
f.writelines(r)
f.close()

