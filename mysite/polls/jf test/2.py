from html.parser import *

#create a subclass and override the handler methods



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Encountered a start tag:", tag)
        global a
        global p
        global o
        global data
        if a >= p:
            print("hijo")
            o=o+'1'
        if p > a:
            print("hermano")
            o=o+'2'
        data = data + tag + '\n'
        p = a
        a = a+1

    def handle_endtag(self, tag):
        print ("Encountered an end tag :", tag)
        global a
        global p
        global o
        global data
        if a>p:
            print("cierro hermano")
            o=o+'3'
        if p>a:
            print("cierro nivel")
            o=o+'4'
#        data = data + tag + '\n'
        p = a
        a = a-1
        

#    def handle_data(self, data):
#        print ("Encountered some data :", data)

# instantiate the parser and fed it some HTML

data = '\n'
o = '\n'
p = 0
a = 0
f=open("404.html","r")
s=f.read()
parser = MyHTMLParser()
parser.feed(s)
o=o + data
print(o)
