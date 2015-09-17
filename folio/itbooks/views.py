from django.shortcuts import render_to_response
from .models import Book, SearchTag
from django.shortcuts import RequestContext, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    title = 'Download Free Books'
    books = Book.objects.all().order_by('?')[:12]
    recent_books = Book.objects.all().order_by('-date')[:16]

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def itbook_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    title = book.title
    return render_to_response('book.html', locals(), context_instance=RequestContext(request))

def google_search(request):
    title = 'google search'
    return render_to_response('googlesearch.html', locals(), context_instance=RequestContext(request))


def search_result(request):
    recent_books = Book.objects.all().order_by('-date')[:16]
    search_query = request.GET.get('query', '')
    title = 'search '+search_query
    if len(search_query) == 0:
        title = 'Error'
        error = 1
        heading = 'Error: Empty Query'
        return render_to_response('searchresults.html', locals(), context_instance=RequestContext(request))

    if len(search_query) <= 2:
        title = 'Error'
        error = 2
        heading = 'Error: Not Enough Characters'
        return render_to_response('searchresults.html', locals(), context_instance=RequestContext(request))
    SearchTag.objects.create(name=search_query)
    heading = 'Results for '+search_query
    meta_description = '%s books in folio.co.in'%search_query
    books =  Book.objects.filter(title__icontains=search_query)
    paginator = Paginator(books, 12)
    page_num = request.GET.get('page', 1)
    page = paginator.page(page_num)

    if not books:
        books = None
        return render_to_response('searchresults.html', locals(), context_instance=RequestContext(request))


    ctx = {
        'query': search_query,
        'title' : title,
        'page' : page,
        'heading' : heading,
        'meta_description' : meta_description
    }
    return render_to_response('searchresults.html', ctx, context_instance=RequestContext(request))
