from django.contrib.sitemaps import Sitemap
from .models import Book

class BookSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Book.objects.all()

    def lastmod(self, obj):
        return obj.date

    def changefreq(self, obj):
        return "daily"