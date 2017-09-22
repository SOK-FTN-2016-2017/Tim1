import sys
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

#        global round
#        global openings
#        global o
#        global data

        if round == 0:
            openings.append(tag)
        else:
            if not openings.count(tag):
#                o=o+'O'
                olist.append('O')
#                data = data + tag + '\n'
                datalist.append(tag)
                datalist.append('\n')
                if (len(attrs) > 0) and (tag !='script'):
                    i = 0
                    while i < len(attrs):
#                        o = o + 'O' + 'D'
                        olist.append('O')
                        olist.append('D')
                        if (len(attrs[i]) > 1) and (attrs[i][1]!= None):
                            if (attrs[i][1].find('"') == -1):
#                                data = data + attrs[i][0] + ': ' + attrs[i][1] + '\n'
                                datalist.append(attrs[i][0])
                                datalist.append(': ')
                                datalist.append(attrs[i][1])
                                datalist.append('\n')
                            else:
#                                data = data + attrs[i][0] + '\n'
                                datalist.append(attrs[i][0])
                                datalist.append('\n')
                        else:
#                            data = data + attrs[i][0] + '\n'
                            datalist.append(attrs[i][0])
                            datalist.append('\n')
                        i += 1



    #######################################################################################

    def handle_endtag(self, tag):
 #       global round
 #       global endings
#        global o
#        global data


        print (t)

        if round == 0:
          endings.append(tag)
        else:
            if not endings.count(tag):
#                o=o+'D'
                olist.append('D')
###################################################################################################

#data = '\n'
#o = ''
#p = ''
t=[1]
olist=[]
datalist=[]
openings=[]
endings=[]
round=0

f=open(sys.argv[1],"r")
s=f.read()
parser = MyHTMLParser()
parser.feed(s)


round+=1

# copy=openings[:]
rep=[]
j=0
for j in endings:
    try:
        openings.remove(j)
    except ValueError:
        # print('no esta', j)
        rep.append(j)

openings.sort()
rep.sort()

j=0
k=len(openings)-1
while j<k:
    if openings[j] == openings[j + 1]:
        openings.pop(j)
        j -= 1
        k = len(openings)-1
    j+=1

j=0
k=len(rep)-1
while j<k:
    if rep[j] == rep[j + 1]:
        rep.pop(j)
        j -= 1
        k = len(rep)-1
    j+=1
openings.extend(rep)
endings=openings[:]

parser.feed(s)

#n=0
# print(o)
#while n<(len(o)-1):
#    if ((o[n]=='O')and(o[n+1]=='O')):
#        p=p+'1'
#    elif ((o[n]=='O')and(o[n+1]=='D')):
#        p=p+'2'
#    elif ((o[n]=='D')and(o[n+1]=='O')):
#        p=p+'3'
#    else:
#        p=p+'4'
#    n+=1

#p=p + data
o2=''
data2=''
for a in olist:
    o2=o2+a
n=0
p2=''
# print(o)
while n<(len(o2)-1):
    if ((o2[n]=='O')and(o2[n+1]=='O')):
        p2=p2+'1'
    elif ((o2[n]=='O')and(o2[n+1]=='D')):
        p2=p2+'2'
    elif ((o2[n]=='D')and(o2[n+1]=='O')):
        p2=p2+'3'
    else:
        p2=p2+'4'
    n+=1

p2=p2+'\n'
for a in datalist:
    p2=p2+a
#print(p)
#print(p)
print(p2)

outfile = open('MiddleFile', 'w')
outfile.write(p2)
outfile.close()


