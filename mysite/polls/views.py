from django.http import HttpResponse


def index(request):
    return HttpResponse("I gope it works.")