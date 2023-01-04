from django.shortcuts import render,get_object_or_404
from .models import Book

# Create your views here.

def showBooKList(request):
    Books = Book.objects.all()
    return render(request,'BookOutlet/home.html',{'Books':Books})


def detailPage(request,id):
    # book = Book.objects.all().get(pk=id)                 # to fetch id from database we can use id or pk(primary key)
    # if id not match it push and exception "Book matching query does not exist."
    # so we have to handle this exception and return 404 page 
    # use method get_object_or_404 method, if object found, return it to book object or it automatically 404 error.
    book = get_object_or_404(Book, pk=id)
    return render(request,'BookOutlet/detail.html',{'book':book})