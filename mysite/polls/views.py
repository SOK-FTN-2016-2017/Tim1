from django.http import HttpResponse
#from django.template import Context, loader
#from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Working poll")
    #return render_to_response('test/index.html')
    #template = loader.get_template("test/index.html")
    #return HttpResponse(template.render())