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