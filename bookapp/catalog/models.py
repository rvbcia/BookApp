from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

# Create your models here.


class BookModel(models.Model):
    # Fields
    author = models.TextField(help_text='Enter authors name and surname')
    title = models.TextField(help_text='Enter title')
    pub_date = models.DateField()
    ISBN = models.CharField(max_length=13, unique=True)
    no_pages = models.TextField()
    cover = models.URLField()
    language = CountryField()

    # Metadata
    class Meta:
        ordering = ['-pub_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.ISBN)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title
