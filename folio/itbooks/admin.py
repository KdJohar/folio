from django.contrib import admin
from .models import GetBook, Book
# Register your models here.


class GetBooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', )
    search_fields = ('title', 'url', )


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'isbn', 'download', 'date', 'featured','most_downloaded',)
    list_filter = ('publisher', 'featured', 'most_downloaded', 'date',)
    search_fields = ('title', 'isbn', 'download', 'date',)

admin.site.register(Book, BookAdmin)
admin.site.register(GetBook, GetBooksAdmin)