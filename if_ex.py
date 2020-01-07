
a=0
if a==10:
    print('a=10')
elif a>10:
    print('a>10')
else:
    print('a<10')

s='python'
if 'yt' in s:
    print('sustring present')
if not s.startswith('java'):
    print('not java')
if s!='c++':
    print('not c++')
if s[1:3]=='yt':
    print('present')
d={'a':10,'b':20}
if 20 in d.values():
    print('20 found')
if ('a',10) in d.items():
    print("a found")