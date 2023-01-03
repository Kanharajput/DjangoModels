"# BookStore" 
About inserting data in sqlite3 database.

insert data using terminal:
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