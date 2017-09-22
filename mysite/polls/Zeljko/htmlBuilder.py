def htmlBuilder ( dir ):

    import sys
    from html.parser import HTMLParser


    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):

            global round
            global openings
            global o
            global data

            if round == 0:
                openings.append(tag)
            else:
                if not openings.count(tag):
                    o=o+'O'
                    data = data + tag + '\n'
                    if (len(attrs) > 0) and (tag !='script'):
                        i = 0
                        while i < len(attrs):
                            o = o + 'O' + 'D'
                            if (len(attrs[i]) > 1) and (attrs[i][1]!= None):
                                if (attrs[i][1].find('"') == -1):
                                    data = data + attrs[i][0] + ': ' + attrs[i][1] + '\n'
                                else:
                                    data = data + attrs[i][0] + '\n'
                            else:
                                data = data + attrs[i][0] + '\n'
                            i += 1



        #######################################################################################

        def handle_endtag(self, tag):
            global round
            global endings
            global o
            global data


            if round == 0:
              endings.append(tag)
            else:
                if not endings.count(tag):
                    o=o+'D'

    data = '\n'
    o = ''
    p = ''
    openings=[]
    endings=[]
    round=0

    f=open(dir,"r")
    s=f.read()
    parser = MyHTMLParser()
    parser.feed(s)


    round+=1
    rep=[]
    j=0
    for j in endings:
        try:
            openings.remove(j)
        except ValueError:
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

    n=0
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

    outfile = open('MiddleFile', 'w')
    outfile.write(p)
    outfile.close()


htmlBuilder("elpais.html")