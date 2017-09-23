def htmlMaker(direc):
    import sys
    from polls.Zeljko.jsonmaker import maker as fn
#    from jsonmaker import maker as  fn

    from html.parser import HTMLParser
    from django.utils.encoding import force_bytes

    def __str__(self):
        return force_bytes(self.name)

    def __unicode__(self):
        return self.name

    class MyHTMLParser(HTMLParser):

        def handle_starttag(self, tag, attrs):
            if round == 0:
                openings.append(tag)
            else:
                if not openings.count(tag):
                    olist.append('O')
                    datalist.append(tag)
                    datalist.append('\n')
                    if (len(attrs) > 0) and (tag !='script'):
                        i = 0
                        while i < len(attrs):
                            olist.append('O')
                            olist.append('D')
                            if (len(attrs[i]) > 1) and (attrs[i][1]!= None):
                                if (attrs[i][1].find('"') == -1):
                                    datalist.append(attrs[i][0])
                                    datalist.append(': ')
                                    datalist.append(attrs[i][1])
                                    datalist.append('\n')
                                else:
                                    datalist.append(attrs[i][0])
                                    datalist.append('\n')
                            else:
                                datalist.append(attrs[i][0])
                                datalist.append('\n')
                            i += 1



        #######################################################################################

        def handle_endtag(self, tag):

            print (t)

            if round == 0:
              endings.append(tag)
            else:
                if not endings.count(tag):
                    olist.append('D')
    ##################################################################################################

    t=[1]
    olist=[]
    datalist=[]
    openings=[]
    endings=[]
    round=0

    f=open(direc,"r")
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

    o2=''
    data2=''
    for a in olist:
        o2=o2+a
    n=0
    p2=''

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

    print(p2)
    json=fn(str(p2))

    outfile = open('polls/static/flare.json', 'w')
   # outfile = open('../static/flare.json','w')
    outfile.write(json)
    outfile.close()