from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Book
from .models import Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/templates/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/templates/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
    
