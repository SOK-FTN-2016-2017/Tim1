from html.parser import *

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Encountered a start tag:", tag)
        global o
        global data

#        if tag != 'meta'
#            o=o+'O'
#            data = data + tag + '\n'

        o=o+'O'
        data = data + tag + '\n'

    def handle_endtag(self, tag):
        print ("Encountered an end tag :", tag)

        global o
        global data

#        if tag != 'meta'
#            o=o+'O'


        o=o+'D'

   
data = '\n'
o = ''
p = ''

f=open("404.html","r")
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

