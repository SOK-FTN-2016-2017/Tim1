from django.http import HttpResponse


def index(request):
    #return HttpResponse("Working poll")
    return render_to_response('polls/test/index.html')