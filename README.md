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