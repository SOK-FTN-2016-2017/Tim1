


input = open('MiddleFile', 'r')

s = ''

for a in input.readline():
    # print ("a=",a[0])
    if a[0]=='1':
       s = s+ '{\n "name": "'+ input.readline()
       s = s[:len(s)-1] +'",\n"children": [\n    '
    if a[0]=='2':
       s=s+'\n     {"name": "'+input.readline()
       s = s[:len(s)-1] + '"'
    if a[0]=='3':
       s=s+'},'
    if a[0]=='4':
       s=s+'}\n]\n'
s=s+'}'

input.close
print (s)

outfile = open('../static/flare.json', 'w') # Indicamos el valor 'w'.
outfile.write(s)
outfile.close()
