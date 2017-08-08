
import os
from os.path import join
for root, dirs, files in os.walk('Tree test'):
    #print(dirs)
    #print(files)
    print (root)
    print ("Files unique children", files)
    print (dirs)
    #print (dirs)
    #print (type(dirs))
    dicta={root:{}}
    dicta[root]

    for a in list
    	print ('name:{', a, ' }')
    print(',')


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