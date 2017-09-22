from polls.Zeljko import treeBuilder as tools
from polls.Zeljko import htmlBuilder as utils
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os
p='f'
outfile = open('pco.pdo', 'w')
outfile.write(p)
outfile.close()

def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        b = request.POST['which_choice']
        a = request.POST['Path']
        if b == '1':
            tools.treeBuilder(a)
        else:
            utils.htmlMaker(a)
    return render(request, 'index.html')
