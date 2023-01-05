from django.contrib import admin
from .models import Book,Author,Address


'''
BlogAdmin is class thrugh which we can configure the admin settings. BlogAdmin can we any name desired by us but the constructor value is fixed admin.ModelAdmin.



'''
class BookAdmin(admin.ModelAdmin):
    # predefined slug when user type the title into the field then automatically the slug should be pop-up to slug field
    # as slug is readonly then we can't prepolute it because it prepopulating actually we are writing so we have remove it from readonly_fields
    # now slug is prepopulated so we can remove that save method because it prepopulated then user click save to save the slug which is in admin form their is no need of overriding save method to create slug.
    # if we don't have admin panel then that save method is the only option to create slug.
    # https://docs.djangoproject.com/en/4.1/ref/contrib/admin/  check this site to configure admin panel
    prepopulated_fields = {"slug":("title",)}       # passded title in tuple to slug we can pass more then one field to create slug
    list_display = ("title","rating",)             # it show column title and rating value for each entry
    list_filter = ("rating","author",)              # show up an filter menu with options rating and author to filter entries

# Register your models here.
# now the book model is registered and we can see it now in admin panel
# also we can edit previously entered data and also we can add some new entries to it
admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)

