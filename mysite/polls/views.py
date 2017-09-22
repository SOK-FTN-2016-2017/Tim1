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
            print('Selector')
        b = request.POST['which_choice']
        a = request.POST['Path']
        if b == '1':
            tools.treeBuilder(a)
        else:
            utils.htmlMaker(a)
	return render(request, 'index.html')
