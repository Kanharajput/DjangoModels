from django.shortcuts import render,get_object_or_404
from .models import Book
from django.db.models import Avg, Min

# Create your views here.

def showBooKList(request):
    Books = Book.objects.all().order_by("rating")      #order_by("-rating") order the data in descending order
    no_of_books = Books.count()           # return the count of books/ entries in the database 
    aggre_dict = Books.aggregate(Avg("rating"),Min("rating"))           # aggregate return a dictionary so that multiple operation can perform via a single statement
    return render(request,'BookOutlet/home.html',{
        'Books':Books,
        'no_of_books':no_of_books,
        'aggre_dict':aggre_dict
        })


def detailPage(request,slug_in_url):
    # book = Book.objects.all().get(pk=id)                 # to fetch id from database we can use id or pk(primary key)
    # if id not match it push and exception "Book matching query does not exist."
    # so we have to handle this exception and return 404 page 
    # use method get_object_or_404 method, if object found, return it to book object or it automatically 404 error.
    book = get_object_or_404(Book, slug=slug_in_url)
    return render(request,'BookOutlet/detail.html',{'book':book})