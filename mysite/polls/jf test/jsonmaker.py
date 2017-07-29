


input = open('MiddleFile', 'r')
s = '{\n "name": "'+ input.readline()+'"'


for a in input.readline():
    print ("a=",a[0])
    if a[0]=='1':
       s=s+',\n"children": [\n    {\n     "name": "'+input.readline()+'"'
    if a[0]=='2':
       s=s+',\n{"name": "'+input.readline()+'"}'
    if a[0]=='3':
       s=s#+','
    if a[0]=='4':
       s=s+']\n}'

input.close
print (s)

