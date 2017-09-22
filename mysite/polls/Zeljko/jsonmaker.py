def maker(seed):
    lines = seed.split('\n')
    data = lines[1:]
    master = lines[0]
    s = ''
    for a in master:
        if a[0]=='1':
           s = s+ '{\n "name": "' + data.pop(0)
           s = s[:len(s)] +'",\n"children": [\n    '
        if a[0]=='2':
           s=s+'\n     {"name": "' + data.pop(0)
           s = s[:len(s)] + '"'
        if a[0]=='3':
           s=s+'},'
        if a[0]=='4':
           s=s+'}\n]\n'
    s=s+'}'

    print (s)
    return s
