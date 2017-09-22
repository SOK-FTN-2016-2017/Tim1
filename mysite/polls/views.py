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
from Zeljko import htmlBuilder as utils
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os

def index(request):
    return render(request, 'index.html')

def submit(request):
	if request.method == 'POST':
            print('Por que me haces esto?')
        b = request.POST['which_choice']
        a = request.POST['Path']
        if b == '1':
            tools.treeBuilder(a)
        else:
            utils.htmlMaker(a)
	return render(request, 'index.html')
