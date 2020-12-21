from django.shortcuts import render
from .models import BookModel

# Create your views here.


def index(request):
    """View function for home page of site."""

    num_books = BookModel.objects.all().count()
    books_list = BookModel.objects.order_by('-pub_date')

    context = {
        'num_books': num_books,
        'books_list': books_list,
    }
    return render(request, 'index.html', context=context)
