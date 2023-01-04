from django.shortcuts import render
from .models import Book

# Create your views here.

def showBooKList(request):
    Books = Book.objects.all()
    return render(request,'BookOutlet/home.html',{'Books':Books})