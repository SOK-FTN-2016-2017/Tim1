
import os
from os.path import join
a = dict()
startpath = 'Tree test'
for root, dirs, files in os.walk(startpath):
    #print(dirs)
    #print(files)
    #print (root)
    #print ("Files unique children", files)
    #print (dirs)
    #print (dirs)
    #print (type(dirs))
    level = root.replace(startpath, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print('{}{}/'.format(indent, os.path.basename(root)))
    a[root.split("\\")[-1]] = 1
    level = root.replace(startpath, '').count(os.sep)
    subindent = ' ' * 4 * (level + 1)
    for f in files:
      print('{}{}'.format(subindent, f))
    '''
    print ('aaaaaa')
    print ('level is', level)
    '''
    '''
    print(type(root))
    print(type(dirs))
    print(type(files))
    '''

print ('"Hola"')
print(a.keys())
#print (a.split("\\")[-1])

'''
escribir con listas
'''


'''


import os

def list_files(startpath):
  for root, dirs, files in os.walk(startpath):
    level = root.replace(startpath, '').count(os.sep)
    indent = ' ' * 4 * (level)
    print('{}{}/'.format(indent, os.path.basename(root)))
    subindent = ' ' * 4 * (level + 1)
    for f in files:
      print('{}{}'.format(subindent, f))

list_files(".")

list_files('.').dirname
'''