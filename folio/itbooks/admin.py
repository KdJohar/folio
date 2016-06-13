from django.contrib import admin
from .models import GetBook, Book, Tag, SearchTag, DownloadBook, SeoMetaData, Category
# Register your models here.


class GetBooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', )
    search_fields = ('title', 'url', )


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'isbn', 'download', 'date', 'featured','most_downloaded',)
    list_filter = ('publisher', 'featured', 'most_downloaded', 'date', 'category', )
    search_fields = ('title', 'isbn', 'download', 'date',)

class SearchAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', )
    list_filter = ('date',)

class DownloadAdmin(admin.ModelAdmin):

    list_display = ('book', 'download')
    search_fields = ('book__title', )

class SeoMetaDataAdmin(admin.ModelAdmin):

    list_display = ('book', 'seo_done', )
    search_fields = ('book__title', )
    list_filter = ('seo_done'),
    list_editable = ('seo_done', )

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Book, BookAdmin)
admin.site.register(GetBook, GetBooksAdmin)
admin.site.register(Tag)
admin.site.register(SearchTag, SearchAdmin)
admin.site.register(DownloadBook, DownloadAdmin)
admin.site.register(SeoMetaData, SeoMetaDataAdmin)
admin.site.register(Category, CategoryAdmin)