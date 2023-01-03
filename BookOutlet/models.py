from django.db import models

# Create your models here.
# in django we don't have to write the sql queries django do it for us
# using models

# this Book class is used as a name of table in plural form , Books
class Book(models.Model):
    # id field is automatically created by django and it also increment with each new row
    title = models.CharField(max_length=50)          # in title field we can only insert char type data
    rating = models.IntegerField()                 # rating column have integer values

'''
we created a db.sqlite3 file in the base folder, sqlite3 is the database and it is able to work with only a file. So we successully set a database but we have to also link it in settings.py but for sqlite3 it already done by the django.

and app name to installed app in settings.py file so that the app is detected at a time of migrations
because django only know the base project folder any change out of it we have to add it in installed apps.

AFter this we have to run two commands 
1. python manage.py makemigrations
        -> this will create a file in migrations folder of this app and it have commands which are in sql. Means it is ready to apply all commands on database.

2. python manage.py migrate 
        -> this will apply all the sql commands to database and also some other commands which are needed by the apps which are added in installed apps, as there code is not showing up because django handles them.

Run this two commands after performing any change in models file
'''