from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse
from django.utils.text import slugify                # used to slug the string

# Create your models here.
# in django we don't have to write the sql queries django do it for us
# using models

# this Book class is used as a name of table in plural form , Books
class Book(models.Model):
    # id field is automatically created by django and it also increment with each new row
    title = models.CharField(max_length=50)          # in title field we can only insert char type data
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])                 # if value is greater or less than 5 and 1 then it will show a validation error
    # as we are creating this two fields after inserting some data in database so we have enter some default data or null value to previously added entries for this columns
    author = models.CharField(max_length=50,null=True)             # it set None when author field is not provided
    is_bestselling = models.BooleanField(default=False)            # defaultly the book is not best selling
    # blank=True because if it is not django make this field required and not let us  to save the data
    # editable=False is also an another way to tweak this sitution, it just hide the field from django admin form of taking data from owner
    slug = models.SlugField(default="",blank=True, null=False, db_index=True)                 # used to create slug like harry-potter-1 because using id as a slug is not a usual  also we set default="" for previously added entries , know about db_index in readme
    

    # as user is not enter the slug value we create it using title of the entry so we are overriding save method to enter slug field at the same time
    # we are creating our slug using title 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)            # so title harry potter then after slugify it is harry-potter
        super().save(*args,**kwargs)


    # this will create a url of each entry and we can pass it to href of home page
    # it is also good practise because we don't need to create path each time we simple call this 
    # method from a entry and we get back an url
    def get_absolute_url(self):
        return reverse("detail-url", args=[self.slug])
    
    
    # this method is used to name the instace at a time of showing row data
    def __str__(self):
        return f"{self.title} ({self.rating})"


'''
we created a db.sqlite3 file in the base folder, sqlite3 is the database and it is able to work with only a file. So we successully set a database but we have to also link it in settings.py but for sqlite3 it already done by the django.

and app name to installed app in settings.py file so that the app is detected at a time of migrations
because django only know the base project folder any change out of it we have to add it in installed apps.

AFter this we have to run two commands 
1. python manage.py makemigrations
        -> this will create a file in migrations folder of this app and it have commands which are in sql. Means it is ready to apply all commands on database.

2. python manage.py migrate 
        -> this will apply all the sql commands to database and also some other commands which are needed by the apps which are added in installed apps, as there code is not showing up because django handles them.

Run this two commands after performing any change in models file and when we change schema if we add any function then there is not need to perform migration commands
'''


