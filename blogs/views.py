from urllib import response
from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    return render(request,"index.html")

def news(request):
    response=requests.get('https://tech-news3.p.rapidapi.com/nineto5mac/?rapidapi-key=1f6d397b61mshec934a43212edd1p1ae62cjsn734f39016558').json()
    return render(request,'news.html',{'response':response})

def about(request):
    return render(request,"about.html")