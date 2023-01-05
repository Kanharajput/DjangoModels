"# BookStore" 
About inserting data in sqlite3 database.

INSERT DATA USING TERMINAL:
1. python manage.py shell
    -> this will open up a shell to perform operations

2. from BookOutlet.models import Book
    -> import the book class

3. harry_potter = Book(title="Harry Potter and the Philosopher's Stone",rating=5)
    -> this will create a sql command with data passed

4. harrry_potter.save()
    -> save the data in the database

Repeat from step 3 to insert more data

To see the data in shell use command:
Book.objects.all()
    -> output : <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
    Here each row is concluded as object

After adding __str__ method in models. output of Book.objects.all() is
    -> <QuerySet [<Book: Harry Potter and the Philosopher's Stone (5)>, <Book: Data Structure and Algorithms made easy (4)>]>

UPDATE DATA TO PREVIOUSLY ADDED ENTRIES 
1. python manage.py shell
    -> this will open up a shell to perform operations

2. from BookOutlet.models import Book
    -> import the book class

3. hr = Book.objects.all()[0]
    -> this will return the first entry to the hr

4. hr.title
    -> this will print "Harry Potter and the Philosopher's Stone"

5. hr.author = "J.K. Rowling"
    -> this will set the author value of this row to J.K. Rowling
    this will not make change in database to save this updation we have to run one more command

6. hr.save()
    -> this will save the changes in database


DELETE THE DATA
1. python manage.py shell
    -> this will open up a shell to perform operations

2. from BookOutlet.models import Book
    -> import the book class

3. ds = Book.objects.all()[1]
    -> this will retun the second row as object

4. ds.delete()
    -> this will delete this row


CREATE METHOD TO ADD NEW ROW IN BOOK TABLE
-> 1 and 2 step is same

3. Book.create(title="lord of the rings",rating=4,author="J. R. R. Tolkien",is_bestselling="True")
    -> don't need to run the save command it automatically save after pressing enter

GET METHOD OF Book.Objects.all() to get the selected data
-> 1 and 2 step is same

3. Book.objects.all().get(id=1)
    -> <Book: Harry Potter and the Philosopher's Stone (5)>

4. Book.objects.all().get(title="Kanha's Story")
    -> output : <Book: Kanha's Story (2)>
    get method will not work when their are two rows found for a same key value

5. Book.objects.all().filter(title__contains="harry",rating=5)
    output : <QuerySet [<Book: Harry Potter and the Philosopher's Stone (5)>]>
    -> in filter we can write more then one condition
    -> here contains is modifier provided by django
    -> one more modifier is __lt which is less than, and __lte is less than equal
    -> one more modifier is __gt which is greater than, and __gte is greater than equal
    -> check this site to know more about modifiers https://www.w3schools.com/django/django_queryset_filter.php

OR CONDITION 
-> 1 and 2 step is same

3. from django.db.models import Q
    -> inbuilt class which let us write queries with or conditio

4. Book.objects.all().filter(Q(title__contains="harry") | Q(rating__lt=3))
    -> output :<QuerySet [<Book: Harry Potter and the Philosopher's Stone (5)>, <Book: Kanha's Story (2)>, <Book: Some title (2)>]>

WRITING OR CONDTION WITH AND CONDITION

5. Book.objects.all().filter(Q(title__contains="harry") | Q(rating__lt=3), Q(author__contains="J.K. Rowling"))
    -> output : <QuerySet [<Book: Harry Potter and the Philosopher's Stone (5)>]>   
    if want to write and without Q then always write it after or condition then only it work if you put in before or condition then it will show error.

    -> Query : Book.objects.all().filter(author__contains="J.K. Rowling", Q(title__contains="harry") | Q(rating__lt=3))
    OUTPUT : File "<console>", line 1
                SyntaxError: positional argument follows keyword argument


DATABASE PERFORMANCE
    best_sellers = Book.objects.all().filter(is_bestselling=True)     
        -> this command will not untill we need the data it is just the query write now
    amazing_best_sellers = best_sellers.filter(rating__gt=4)
        -> we can get the amazing_best_sellers from the best_sellers their is no need to touch the database and it is also a query 
        right now.

        When we print the data, then actually the database is touched
        print(best_sellers)        # now the query is run  and we get the data from database
        print(amazing_best_sellers)       # this time the data is accessed from the database rather then it is just the filter of
                                            best_sellers data.

        So this is how we increase the performance if we directly the data without putting it in variable then each time we have to 
        fetch the data from database. like this 
        print(Book.objects.all().filter(is_bestselling=True))   # data is accesssed from database
        print(Q(Book.objects.all().filter(is_bestselling=True)) | Q(Book.objects.all().filter(rating__gt=4)))   # this time it is also accessed from database


TO CREATE SLUG OF SAVED ENTRIES OF DATABASE:
    1 and 2 step is same
3. Book.objects.get(id=1).save()
    -> as we run save method it create slug as we override the save method

4. Entering new entry will automatically create the slug

DB_INDEX = TRUE, increase the performance database some how make this column values more effiecient to search. Not make all field db_index as db_index then lower the performance it is good for one column which is fetching many times.

WE HAVE A ADMIN PANEL WHICH IS GIVEN BY DJANGO TO PUT DATA IN DATABASE IT IS NOT FOR USER IT IS FOR OWNER OF THE SITE TO PUT SITE NEEDED DATA ON DATABASE
- visit http://127.0.0.1:8000/admin to see the admin panel
- needed login credential, create superuser by command
- python manage.py createsuperuser

FETCHING AND STORING DATA IN MULTIPLE TABLE VIA SHELL :
1. from BookOutlet.models import Author
2. jkrowling = Author(first_name="J.K.", last_name="Rowling")
3. jkrowling.save()
    -> this will save the entry in Author table

4. from BookOutlet.models import Book
5. hr = Book(title="Harry Potter 1",rating =5, is_bestselling=True,slug="harry-potter-1",author=jkrowling)
6. hr.save()
    -> we simply pass the jkrowling object to the author field not an id , django will automatically do it for us
    -> NOte : remember we deleted that save method so now we have to manually write the slug.

FETCHING DATA:
- harry = Book.objects.all()[0]
- harry.author
    - output : <Author: Author object (1)>  work as normal as working with a field of table but actually author is an another table
- harry.author.first_name
    - Output : 'J.K.'
- harry.author.last_name
    - Output : 'Rowling'

FILTER THE BOOK USING AUTHOR DATA
- book_by_rowling = Book.objects.filter(author__last_name="Rowling")
    - this will return all the books written by rowling in a list each item of list denote a entry.

HOW TO ACCESSING BOOK DATA FROM AUTHOR DATA
- from BookOutlet.models import Author
- jk = Author.objects.filter(first_name="J.K.")
    - we get the entry having first_name = J.K.
- jk.book_set
    - this will put all the entries of book which have foreign key as jk
    - now we can run all the operation which we can apply over objects

- jk.book_set.filter(title__contains="ha")
    - this will return the book entries whose title contains ha, so we are getting data from Book table
    
- we can also create this object from models and set name as we want rather then just book_set, using related_name
- then we can directly check the data related to author jk by just typing jk.books.all()
- but there is a condition we have to get the entry in jk by get only not by filter or index, then only it work

TO RELATE BOOKS WITH AUTHOR THROUGH ADMIN PANEL
- enter books and author entries
- in books entering form their is an option to select author
- all entries of author table are listed their simple select one author to relate it with the book.

AS IT IS ONETOONE RELATION ADMIN PANEL NOT LET US TO PASS SAME ADDRESS FOR TWO DIFFERENT AUTHORS

WORK WITH ONETOONE THROUGH SHELL
- from BookOutlet.models import Address,Author
- adr1 = Address(street="Main road", postal_code=32415,city="Dhar")
- adr1.save()
- auth1 = Author.objects.get(first_name="J.K.")
- auth1.address = adr1        this is how we link a address to the author

getting AUTHOR DATA THROUGH ADDRESS
- adr1.author                      
    - Output : <Author: Kanha Tomar>
    - here we don't need to create related_name django automatically done it . but in one to many field we have to pass it like for author we have book_set.

    DONE WITH ONE TO ONE FIELD

    WHY ManyToManyField not a on_delete
    - because lets suppose one books related with five different countries and after some time book got banned in one country so we delete that country from the database, and if it on_delete then the book entry also deleted from the Book table but the same book is live in that four countries.
    - So to delete one country data django automatically create a third table behind the scene.So for one book if there are five publisher countries then that table contains five rows with only difference of country. 
    - This third table is always there if we are working with ManyToManyFields no matter which framework we are working on.

    WORKING WITH ManyToMany in shell
    - from BookOutlet.models import Book,Country
    - india = Country(name="India", code =001)
    - india.save()
        - this will create a entry in Country table, now link it with Book entries

    - hr1 = Book.objects.all()[0]
    - hr1.published_countries.add(india)
        - as it published_countries can be more then one that'swhy we have add method we can pass more then one country at the same time
    - query_set_india = hr1.published_countries.filter(name="India")
    - india = query_set_india[0]
    - india.name
        - Output : Indi

    HERE ALSO WE CAN GET BOOK DETAILS FROM COUNTRY ENTRIES
    - india = Country.objects.get(name="India")     
    - india.book_set.all()          we can change this book_set by related_name arg in manytomany field
    - query_obj_hr = india.book_set.filter(title="Harry Potter 1")
    - hr = query_obj_hr[0]
    - hr.title
        - Output : 'Harry Potter 1'


CIRCULAR RELATIONS & LAZY RELATIONS 
Sometimes, you might have two models that depend on each other - i.e. you end up with a circular relationship.

Or you have a model that has a relation with itself.

Or you have a model that should have a relation with some built-in model (i.e. built into Django) or a model defined in another application.

Below, you find examples for all three cases that include Django's solution for these kinds of "problems": Lazy relationships. You can also check out the official docs in addition.

1) Two models that have a circular relationship

class Product(models.Model):
  # ... other fields ...
  last_buyer = models.ForeignKey('User')
  
class User(models.Model):
  # ... other fields ...
  created_products = models.ManyToManyField('Product')

In this example, we have multiple relationships between the same two models. Hence we might need to define them in both models. By using the model name as a string instead of a direct reference, Django is able to resolve such dependencies.

2) Relation with the same model

class User(models.Model):
  # ... other fields ...
  friends = models.ManyToManyField('self') 
  
The special self keyword (used as a string value) tells Django that it should form a relationship with (other) instances of the same model.

3) Relationships with other apps and their models (built-in or custom apps)

class Review(models.Model):
  # ... other fields ...
  product = models.ForeignKey('store.Product') # '<appname>.<modelname>'

You can reference models defined in other Django apps (no matter if created by you, via python manage.py startapp <appname> or if it's a built-in or third-party app) by using the app name and then the name of the model inside the app.