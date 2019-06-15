import re

txt = '''
pcevssl.lifecard.co./jp/
/co/LW32
LW3201OP01BL./do/?for/ward/
'''
e = re.findall('/.*?/',txt,re.IGNORECASE|re.MULTILINE)
e2 = []
for i in e:
	e2.append(i[1:-1])
print(e)
print(e2)
