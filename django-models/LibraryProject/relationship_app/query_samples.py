from . import models

book = models.Book
author = models.Author
library = models.Library
librarian = models.Librarian  

def get_books_by_author(author_name):
    try:
        author = models.Author.objects.get(name=author_name)
        return book.objects.filter(author=author)
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
      librarian_instance = models.Librarian.objects.get(library=library_name)
      return librarian_instance.name
    except models.Librarian.DoesNotExist:
      return None


