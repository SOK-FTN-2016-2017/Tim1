import sys
from html.parser import *


class MyHTMLParser(HTMLParser):
    def handle_data(self, dat):
        global cont
        global data
        print('1')
        if (dat[0] != '\n'):# and (dat[0:1] != '  '):
            print('DATA=',dat)
            cont=cont+dat
            data=data[len(data)-1]+'= '+dat[0:15]
        else:
            cont=''
        print('CONT=', cont)

    #######################################################################################
    def handle_starttag(self, tag, attrs):
        print ("2")
        global o
        global data
        global cont
#        if tag != 'meta'
#            o=o+'O'
#            data = data + tag + '\n'



        # o=o+'O'
        # if cont != '':
        #     print ('2cont=', cont)
        #     data = data + tag+': '+cont+'\n'
        # else:
        #     data = data + tag+'\n'
        data = data + tag + '\n'

        print('datra=',data)



#        print ('number of attrs:',len(attrs))
#         if len(attrs) > 0:
#             i=0
#             while i < len(attrs):
#                 o=o+'O'+'D'
# #                print (i)
#  #               print ('number of attrs:', len(attrs))
#                 data=data + attrs[i][0]+': '+attrs[i][1]+'\n'
# #                print ('X')
# #                print ('tam attrs:', len(attrs[2]))
# #                print ("Encountered a attrvs:", attrs)  # tag)
#                 i += 1
    #######################################################################################

    def handle_endtag(self, tag):
#        print ("Encountered an end tag :", tag)

        global o
        global data

#        if tag != 'meta'
#            o=o+'O'

        o=o+'D'


data = '\n'
o = ''
p = ''
cont = ''

f=open(sys.argv[1],"r")
s=f.read()
parser = MyHTMLParser()
parser.feed(s)

n=0
#print(o)
while n<(len(o)-1):
    if ((o[n]=='O')and(o[n+1]=='O')):
        p=p+'1'
    elif ((o[n]=='O')and(o[n+1]=='D')):
        p=p+'2'
    elif ((o[n]=='D')and(o[n+1]=='O')):
        p=p+'3'
    else:
        p=p+'4'
    n+=1

p=p + data

print(data)
# print(cont)

outfile = open('MiddleFile', 'w')
outfile.write(p)
outfile.close()
