from django.shortcuts import render_to_response
from .models import Book, SearchTag, Tag
from django.shortcuts import RequestContext, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
import json
from .forms import ItSearchForm, SearchForm
from haystack.inputs import AutoQuery
from haystack.query import SearchQuerySet
# Create your views here.

def home(request):
    title = 'Download Free Books'
    books = Book.objects.all().order_by('?')[:8]
    datalist = Book.objects.all()
    recent_books = Book.objects.all().order_by('-date')[:16]
    tags = Tag.objects.all()
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def itbooks(request):
    title = 'Download Free Books'
    books = Book.objects.all().order_by('-date')[:24]
    tags = Tag.objects.all()
    return render_to_response('itbooks.html', locals(), context_instance=RequestContext(request))

def itbook_detail(request, slug):
    datalist = Book.objects.all()
    book = get_object_or_404(Book, slug=slug)
    title = book.title
    return render_to_response('book.html', locals(), context_instance=RequestContext(request))

def google_search(request):
    title = 'google search'
    return render_to_response('googlesearch.html', locals(), context_instance=RequestContext(request))


def search_result(request):
    search_query = request.GET.get('query', '')
    tags = Tag.objects.all()
    if not search_query == ' ':
        SearchTag.objects.create(name=search_query)
        books = SearchQuerySet().filter(title=AutoQuery(search_query)).load_all()
        paginator = Paginator(books, 12)
        page_num = request.GET.get('page', 1)
        page = paginator.page(page_num)
    ctx = {
        'tags':tags,
        'query': search_query,
        'page' : page,
        'count':len(books)
    }
    return render_to_response('searchresults.html', ctx, context_instance=RequestContext(request))

def autocomplete(request):
    if request.method == 'GET':
        query = request.GET.get('input', '')
        suggestions = Book.objects.filter(title__icontains=query)[:7]
        suggestions_data = [r.title for r in suggestions]
        results = json.dumps({'title':suggestions_data})
        return HttpResponse(results, content_type='application/json')
