from django import forms

from .models import BookModel


class AddBook(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'ISBN', 'pub_date', 'no_pages', 'cover', 'language']
