from django.shortcuts import render_to_response, redirect
from .models import Book, SearchTag, Tag, DownloadBook, Category
from django.shortcuts import RequestContext, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
import json
import urllib
from haystack.inputs import Raw
from .forms import ItSearchForm, SearchForm
from haystack.inputs import AutoQuery
from haystack.query import SearchQuerySet
import json
# Create your views here.

def home(request):
    books = Book.objects.all().order_by('?')[:10]
    tags = Category.objects.all()
    return render_to_response('itbook/index.html', locals(), context_instance=RequestContext(request))

def all_category(request):
    categories = Category.objects.all()
    title = 'Categories'
    return render_to_response('itbook/all_categories.html', locals(), context_instance=RequestContext(request))

def itbook_detail(request, slug):
    datalist = Book.objects.all()
    book = get_object_or_404(Book, slug=slug)
    tags = Category.objects.all()
    title = book.title
    return render_to_response('itbook/bookdetail.html', locals(), context_instance=RequestContext(request))

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    title = category.name
    books = Book.objects.filter(category=category.id)
    paginator = Paginator(books, 10)
    page_num = request.GET.get('page', 1)
    page = paginator.page(page_num)
    page_count = 10*int(page_num)


    ctx = {
        'page_count': page_count,
        'page': page,
        'category': category,
        'title': 'Download '+title + ' ebooks'
        #'title': search_query + ' search','ebooks'
    }

    return render_to_response('itbook/category.html', locals(), context_instance=RequestContext(request))


def search_result(request):
    search_query = request.GET.get('query', '')
    tags = Tag.objects.all()
    suggestions = SearchQuerySet().spelling_suggestion(search_query)
    if not search_query == ' ':
        books = SearchQuerySet().filter(title=Raw(urllib.unquote(search_query).decode('utf8') ))
        paginator = Paginator(books, 10)
        page_num = request.GET.get('page', 1)
        page = paginator.page(page_num)
    ctx = {
        'tags':tags,
        'query': urllib.unquote(search_query).decode('utf8'),
        'page' : page,
        'count':len(books),
        'title': 'search for '+'search_query+' 'ebooks',
        #'suggestions' : suggestions
    }
    return render_to_response('itbook/search.html', ctx, context_instance=RequestContext(request))

def autocomplete(request):
    if request.method == 'GET':
        query = request.GET.get('input', '')
        suggestions = Book.objects.filter(title__icontains=query)[:7]
        suggestions_data = [r.title for r in suggestions]
        results = json.dumps({'title':suggestions_data})
        return HttpResponse(results, content_type='application/json')

def createsearchtag(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')

        SearchTag.objects.create(name=name)
        return HttpResponse(json.dumps({'result':'done'}))


def downloaded_book(request):

    if request.method == 'GET':
        obj = request.GET.get('id', '')
        book_obj = DownloadBook.objects.get(book_id=obj)
        print(book_obj)
        book_obj.download += 1
        book_obj.save()

        return HttpResponse(json.dumps({'result': 'done'}))

