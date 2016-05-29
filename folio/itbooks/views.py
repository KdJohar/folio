from django.shortcuts import render_to_response
from .models import Book, SearchTag, Tag
from django.shortcuts import RequestContext, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
import json
import urllib
from haystack.inputs import Raw
from .forms import ItSearchForm, SearchForm
from haystack.inputs import AutoQuery
from haystack.query import SearchQuerySet
# Create your views here.

def home(request):
    books = Book.objects.all().order_by('?')[:10]
    tags = Tag.objects.all()
    return render_to_response('index2.html', locals(), context_instance=RequestContext(request))

def itbook_detail(request, slug):
    datalist = Book.objects.all()
    book = get_object_or_404(Book, slug=slug)
    tags = Tag.objects.all()
    title = book.title
    return render_to_response('new/bookdetail.html', locals(), context_instance=RequestContext(request))

def google_search(request):
    title = 'google search'
    return render_to_response('googlesearch.html', locals(), context_instance=RequestContext(request))


def search_result(request):
    search_query = request.GET.get('query', '')
    tags = Tag.objects.all()
    suggestions = SearchQuerySet().spelling_suggestion(search_query)
    print suggestions
    print '='*10
    if not search_query == ' ':
        SearchTag.objects.create(name=search_query)
        books = SearchQuerySet().filter(title=Raw(urllib.unquote(search_query).decode('utf8') ))
        paginator = Paginator(books, 10)
        page_num = request.GET.get('page', 1)
        page = paginator.page(page_num)
    ctx = {
        'tags':tags,
        'query': urllib.unquote(search_query).decode('utf8'),
        'page' : page,
        'count':len(books),
        'title': search_query+' search',
        #'suggestions' : suggestions
    }
    return render_to_response('searchr.html', ctx, context_instance=RequestContext(request))

def autocomplete(request):
    if request.method == 'GET':
        query = request.GET.get('input', '')
        suggestions = Book.objects.filter(title__icontains=query)[:7]
        suggestions_data = [r.title for r in suggestions]
        results = json.dumps({'title':suggestions_data})
        return HttpResponse(results, content_type='application/json')
