from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse

# Create your models here.
# to understand what happened till now check the previous commit every commit covers a different topic 

# Address table to store address of authors
class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)


# Author table to store author data
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # more good to put address in Author as in real world author have a address not a address has a author
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    # every entry of Author table is represented by it's first and last name
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=50)          
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    # author is now foreign key which point to a entry in author table
    # on_delete tells what to do if pointed entry got deleted from Author table , CASCADE means delete book entry also
    # on_delete=models.SET_NULL, on_delete=models.PROTECT, other options we can use in on_delete
    # delete all the entries, if there's something already in database before migration
    # ForeignKey is for one to many relation
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")                   
    is_bestselling = models.BooleanField(default=False)            
    slug = models.SlugField(default="",blank=True, null=False, db_index=True)
    
    def get_absolute_url(self):
        return reverse("detail-url", args=[self.slug])
    
    
    def __str__(self):
        return f"{self.title} ({self.rating})"

    