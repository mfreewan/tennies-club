from django.http import Http404
from django.shortcuts import render
from django.views import generic

from .models import Author, Book, BookInstance, Genre

# Create your views here.


def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1


    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits' : num_visits,
    }

    return render(request, 'index.html', context=context)

# create view for book list


class BookListView(generic.ListView):
    model = Book
    book_list = 'book_list'   # your own name for the list as a template variable
    template_name = 'main/book_list.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
            # Call the base implementation first to get the context
            context = super(BookListView, self).get_context_data(**kwargs)
            # Create any data and add it to the context
            context['some_data'] = 'This is just some data'
            return context

from django.shortcuts import get_object_or_404


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
                                
        return render(request,  context={'book': book})