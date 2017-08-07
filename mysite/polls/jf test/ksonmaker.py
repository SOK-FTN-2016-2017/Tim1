


input = open('MiddleFile', 'r')

s = '\n'

for a in input.readline():
    print ("a=",a[0])
    if a[0]=='1':
       s = s+ '{\n "name": "'+ input.readline()+'",\n"children": [\n    '
    if a[0]=='2':
       s=s+'\n     {"name": "'+input.readline()+'"'
    if a[0]=='3':
       s=s+'},'
    if a[0]=='4':
       s=s+'}\n]\n'
s=s+'}'

input.close
print (s)

