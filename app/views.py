from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")
def index2(request):
 #   list = [1, 4, 9, 16]
    return render(request, 'index.html', {'lists': (1,2,3,4) })
    

