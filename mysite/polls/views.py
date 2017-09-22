'''
from django.http import HttpResponse
#from django.template import Context, loader
#from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Working poll")
    #return render_to_response('test/index.html')
    #template = loader.get_template("test/index.html")
    #return HttpResponse(template.render())

'''

from Zeljko import treeBuilder as tools
from django.shortcuts import render
from django.http import HttpResponse
#import treeBuilder
import datetime
import os
#import sys
#sys.path.insert(0, 'Zeljko')


def index(request):
    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
# Get the data from the file

#    with open('polls/test/index.html', 'rb') as fp:
   
 #       html = fp.read()
  #     '''
    return render(request, 'index.html')
def submit(request):
	if request.method == 'POST':
		a = request.POST['which_choice']
        if a == '1':
            outfile = open('Option 1', 'w')
            outfile.close()
            tools.treeBuilder('.')
            #os.system("py polls\\Zeljko\\treeBuilder.py")
        elif a == '2':
            outfile = open('Option 2', 'w')
            outfile.close()
        else:
            outfile = open('Nofunciona', 'w')
            outfile.close()
        print(type(a))
	return render(request, 'index.html')