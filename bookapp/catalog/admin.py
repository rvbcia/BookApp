from django.contrib import admin
from .models import BookModel


# Define the admin class
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'ISBN', 'pub_date', 'cover', 'no_pages', 'language']
    list_filter = ['title', 'author', 'language', 'pub_date']
    pass


# Register your models here.
admin.site.register(BookModel, BookAdmin)

