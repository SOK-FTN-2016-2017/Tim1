def treeBuilder(startpath):

    import os
    import sys
    import polls.Zeljko.jsonmaker as parsingtool
    from os.path import join

    if not startpath:
        startpath = '..\..'
    data = ''
    cod = ''
    fin = '0'
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        cod = cod + str(level)
        data = data + os.path.basename(root) + '\n'
        level = root.replace(startpath, '').count(os.sep)
        for f in files:
            cod = cod + str(level+1)
            # path = os.path.join(root, f)
            # size = os.stat(path).st_size
            
            data = data + f + ':Size = ' + str(os.stat(os.path.join(root, f)).st_size) + 'bytes' + '\n'
    cod = cod + '0'
    for i in range(1, len(cod)):
        if cod[i] > cod[i-1]:
            fin = fin[:len(fin)-1] + '12'
        elif cod[i] == cod[i-1]:
            fin = fin + '32'
        else:
            fin = fin + (int(cod[i-1])-int(cod[i]))*'4' + '32'
    fin = fin[:len(fin)-2] + '\n' + data
    json = parsingtool.maker(fin)
    outfile = open('polls/static/flare.json', 'w') 
    outfile.write(json)
    outfile.close()
    