from django.contrib import admin
from .models import Book

# Register your models here.
# now the book model is registered and we can see it now in admin panel
# also we can edit previously entered data and also we can add some new entries to it
admin.site.register(Book) 