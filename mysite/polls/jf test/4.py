import sys
from html.parser import *


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):

        global o
        global data
        if (tag != 'meta') and (tag !='link'):
            o=o+'O'
            data = data + tag + '\n'
#           print ('number of attrs:',len(attrs))
#             if (len(attrs) > 0) and (tag !='script'):
#                 i = 0
#                 print('antesdelwhile nu hiperatt', len(attrs))
#                 while i < len(attrs):
#                     o = o + 'O' + 'D'
#                     print ('i=', i)
#                     print ('number of attrs:', len(attrs[i]))
#                     if len(attrs[i]) > 1:
#                         data = data + attrs[i][0] + ': ' + attrs[i][1] + '\n'
#                     else:
#                         data = data + attrs[i][0] + '\n'
#                     print ('X')
#                     # print ('tam attrs:', len(attrs[2]))
#                     print ("Encountered a attrvs:", attrs)  # tag)
#                     i += 1
        # o=o+'O'
        # data = data + tag+'\n'


    #######################################################################################

    def handle_endtag(self, tag):
#        print ("Encountered an end tag :", tag)

        global o
        global data

        if (tag != 'meta') and (tag !='link'):
            o=o+'D'

        # o=o+'D'


data = '\n'
o = ''
p = ''


f=open(sys.argv[1],"r")
s=f.read()
parser = MyHTMLParser()
parser.feed(s)

n=0
print(o)
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

print(p)

outfile = open('MiddleFile', 'w')
outfile.write(p)
outfile.close()

