from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    return render(request, template_name='corporateanalysis/hello.html')


def corporateanalysis(request):
    return render(request, template_name='corporateanalysis/search/search.html')
