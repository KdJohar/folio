from django.contrib import admin
from .models import GetBook, Book, Tag, SearchTag
# Register your models here.


class GetBooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', )
    search_fields = ('title', 'url', )


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'isbn', 'download', 'date', 'featured','most_downloaded',)
    list_filter = ('publisher', 'featured', 'most_downloaded', 'date',)
    search_fields = ('title', 'isbn', 'download', 'date',)

class SearchAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', )
    list_filter = ('date',)

admin.site.register(Book, BookAdmin)
admin.site.register(GetBook, GetBooksAdmin)
admin.site.register(Tag)
admin.site.register(SearchTag, SearchAdmin)