from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'samsung.html')
def analyze(request):
    text =  request.GET.get('navname')
    text2 = request.GET.get('home')
    text3 = request.GET.get('value')

    params = {'navbar':text , 'home' : text2 , 'analyze' : text3}


    return render(request , 'analyze.html' ,params)