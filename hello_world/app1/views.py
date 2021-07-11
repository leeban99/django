from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'a.html')


def expression(request):
    a = request.post("text1")
    return render(request, 'output.html',{'result':"testing...."})



def profile(request):
    return HttpResponse('<b>profile page</b>')
