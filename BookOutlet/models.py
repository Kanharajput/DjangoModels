from django.db import models

# Create your models here.
# in django we don't have to write the sql queries django do it for us
# using models

# this Book class is used as a name of table in plural form , Books
class Book(models.Model):
    # id field is automatically created by django and it also increment with each new row
    title = models.CharField(max_length=50)          # in title field we can only insert char type data
    rating = models.IntegerField()                 # rating column have integer values
