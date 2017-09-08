import os
from os.path import join

startpath = 'Tree test'
data = ''
#startpath + '\n'
code = ''
state = 0
aux1 = 0
cod = ''
fin = '0'
for root, dirs, files in os.walk(startpath):
    level = root.replace(startpath, '').count(os.sep)
    print (level)
    indent = ' ' * 4 * (level)
    cod = cod + str(level)
    print('{}{}/'.format(indent, os.path.basename(root)))
    data = data + os.path.basename(root) + '\n'
    code = code + '23'
    level = root.replace(startpath, '').count(os.sep)
    subindent = ' ' * 4 * (level + 1)
    #print ('Ficheros', files)
    # if state == level:
    #     aux1 = 1
    # elif state > level:
    #     code = code[:len(code)-2]+(state*'4')+'3'
    # else:
    #     aux1= 1
    # state = level
    i = len(files)
    for f in files:
        if i == len(files):
            code = code[:len(code)-2]+'1'
        #print('longitud', len(files))
        print('{}{}'.format(subindent, f))
        cod = cod + str(level+1)
        data = data + f +'\n'
        code = code + '23'
        i = i-1
        if i == 0 and not dirs:
            # if aux1 == 0:
            code = code[:len(code)-1]+(level*'4')+'3'
            # else:
            # code = code[:len(code)-1]+'43'
            # else:
            #     code = code[:len(code)-1]+'3'

code = code[:len(code)-1]+'4'   
cod = cod + '0'

print(code)
print(data)
print(cod)
for i in range(1, len(cod)):
    if cod[i] > cod[i-1]:
        fin = fin[:len(fin)-1] + '12'
    elif cod[i] == cod[i-1]:
        fin = fin + '32'
    else:
        fin = fin + (int(cod[i-1])-int(cod[i]))*'4' + '32'
print(fin)
fin = fin[:len(fin)-2]
print(fin)
aux = fin + '\n' + data
outfile = open('MiddleFile', 'w') # Indicamos el valor 'w'.
outfile.write(aux)
outfile.close()
