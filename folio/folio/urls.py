"""folio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from itbooks import viewsets
from django.conf import settings
from itbooks.sitemap import BookSitemap

sitemaps = {
    "book": BookSitemap
}

router = DefaultRouter()

router.register(r'getbook', viewsets.GetBookViewset)
router.register(r'book', viewsets.BookViewset)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/1/', include(router.urls)),
    url(r'^$', 'itbooks.views.home', name='home'),
    url(r'^itbook/(?P<slug>[\w-]+)/$', 'itbooks.views.itbook_detail', name='itbook_detail'),
    url(r'^google/$', 'itbooks.views.google_search', name='google_search'),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

]

urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
))