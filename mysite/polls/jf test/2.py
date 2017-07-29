from html.parser import *

#create a subclass and override the handler methods



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Encountered a start tag:", tag)
        global a
        global p
        if a >= p:
            print("hijo")
        if p > a:
            print("hermano")
        p = a
        a = a+1

    def handle_endtag(self, tag):
        print ("Encountered an end tag :", tag)
        global a
        global p
        if a>p:
            print("cierro hermano")
        if p>a:
            print("cierro nivel")
        p = a
        a = a-1
        

#    def handle_data(self, data):
#        print ("Encountered some data :", data)

# instantiate the parser and fed it some HTML


p = 0
a = 0
f=open("404.html","r")
s=f.read()
parser = MyHTMLParser()
parser.feed(s)
