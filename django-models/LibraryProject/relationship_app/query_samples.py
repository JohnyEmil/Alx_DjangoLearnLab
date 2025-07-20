from . import models

book = models.Book
author = models.Author
library = models.Library
librarian = models.Librarian  

def get_books_by_author(author_name):
    try:
        author_instance = models.Author.objects.get(name=author_name)
        return author_instance.book_set.all()
    except models.Author.DoesNotExist:
        return book.objects.none()
    
def get_books_in_library(library_name):
    try:
        library_instance = models.Library.objects.get(name=library_name)
        return library_instance.books.all()
    except models.Library.DoesNotExist:
        return book.objects.none()
    
def get_librarian_of_library(library_name):
    try:
        library_instance = models.Library.objects.get(name=library_name)
        return library_instance.librarian
    except models.Library.DoesNotExist:
        return None
    except models.Librarian.DoesNotExist:
        return None

