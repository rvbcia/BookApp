from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .models import BookModel
from .forms import AddBook
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


def add_book(request):
    # book = BookModel.objects.first()
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            # book.title = form.cleaned_data['title']
            # book.save()
            # form.title = form.cleaned_data['title']
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = AddBook()
    context = {
        'form': form,
        # 'book': book
    }

    return render(request,  'add_book.html', context)


def edit_book(request, pk):
    book_to_edit = BookModel.objects.get(id=pk)
    if request.method == 'POST':
        form = AddBook(instance=book_to_edit, data=request.POST)
        if form.is_valid():
            form.title = form.cleaned_data['title']
            form.author = form.cleaned_data['author']
            form.ISBN = form.cleaned_data['ISBN']
            form.pub_date = form.cleaned_data['pub_date']
            form.no_pages = form.cleaned_data['no_pages']
            form.cover = form.cleaned_data['cover']
            form.language = form.cleaned_data['language']
            form.update()
    else:
        form = AddBook(instance=book_to_edit)
    context = {
        'form': form,
        'book_to_edit': book_to_edit
    }
    return render(request, 'edit_book.html', context)
