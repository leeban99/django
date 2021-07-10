from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'a.html')


def profile(request):
    return HttpResponse('<b>profile page</b>')
