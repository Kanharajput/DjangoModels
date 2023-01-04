from django.shortcuts import render

# Create your views here.

def showBooKList(request):
    return render(request,'BookOutlet/home.html')