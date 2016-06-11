from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import signals
# Create your models here.

class GetBook(models.Model):
    'Keeps track of it books from https://it-ebooks.info/'
    title = models.CharField(max_length=250, unique=True)
    url = models.URLField(unique=True)

    class Meta:
        ordering = ['title']



class Book(models.Model):

    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(null=True)
    image = models.URLField(unique=True, null=True, blank=True)
    publisher = models.CharField(max_length=250, null=True, blank=True)
    author = models.CharField(max_length=250, null=True, blank=True)
    pages = models.CharField(max_length=5, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    download = models.URLField(unique=True, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    featured = models.BooleanField(default=False)
    most_downloaded = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        return reverse ('itbook_detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title

class DownloadBook(models.Model):

    book = models.OneToOneField(Book)
    download = models.IntegerField(default=0)

    def __unicode__(self):
        return self.book.title
    class Meta:
        verbose_name_plural = "Download"
        ordering = ['-download']

class SeoMetaData(models.Model):

    book = models.OneToOneField(Book)
    keywords = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    seo_done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.book.title

    class Meta:
        verbose_name_plural = "Book Page Metadata"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class SearchTag(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

def create_download_seo_for_book(sender, instance, created, **kwargs):
    if created:
        DownloadBook.objects.create(book=instance)
        SeoMetaData.objects.create(book=instance)


signals.post_save.connect(create_download_seo_for_book, sender=Book)