from html.parser import *

#create a subclass and override the handler methods



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Encountered a start tag:", tag)
#        global a
#        global p
        global o
        global data
#        if a >= p:
#            print("hijo")
#            o=o+'1'
#        if p > a:
#            print("hermano")
#            o=o+'2'
        o=o+'O'
        data = data + tag + '\n'
#        p = a
#        a = a+1

    def handle_endtag(self, tag):
        print ("Encountered an end tag :", tag)
 #       global a
 #       global p
        global o
        global data
 #       if a>p:
 #           print("cierro hermano")
 #           o=o+'3'
 #       if p>a:
 #           print("cierro nivel")
 #           o=o+'4'
        o=o+'D'
#        data = data + tag + '\n'
#        p = a
#        a = a-1
        

#    def handle_data(self, data):
#        print ("Encountered some data :", data)

# instantiate the parser and fed it some HTML

data = '\n'
o = ''
p = ''
a = 0
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

outfile = open('MiddleFile', 'w') # Indicamos el valor 'w'.
outfile.write(p)
outfile.close()

