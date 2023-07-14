from django.shortcuts import render

# Create your views here.
def detail(request):
    return render(request,"main/detail.html")
def index(request):
    return render(request,"main/index.html")