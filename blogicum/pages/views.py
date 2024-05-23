from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.
def about(request):
    return render(request, 'pages/about.html')

def rules(request):
    return render(request, 'pages/rules.html')