from django.contrib import admin
from .models import Book


'''
BlogAdmin is class thrugh which we can configure the admin settings. BlogAdmin can we any name desired by us but the constructor value is fixed admin.ModelAdmin.



'''
class BookAdmin(admin.ModelAdmin):
    # this will make the slug field readonly means can't be editable so now we can remove the editable form the slug field
    readonly_fields = ("slug",)    # here we are adding comma because readonyly_fields can be only list or tuple
     


# Register your models here.
# now the book model is registered and we can see it now in admin panel
# also we can edit previously entered data and also we can add some new entries to it
admin.site.register(Book,BookAdmin)

