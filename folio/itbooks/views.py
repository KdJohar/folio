from django.shortcuts import render_to_response
from .models import Book, SearchTag
from django.shortcuts import RequestContext, get_object_or_404
from .forms import SearchForm
# Create your views here.

def home(request):
    books = Book.objects.all().order_by('?')[:12]
    recent_books = Book.objects.all().order_by('-date')[:8]
    form = SearchForm(request.POST)
    if form.is_valid():
        search_query = form.cleaned_data['search']
        books =  Book.objects.filter(title__icontains=search_query)
        if not books:
            books = None
        SearchTag.objects.create(name=search_query)
    else:
        return render_to_response('index.html', locals(), context_instance=RequestContext(request))

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def itbook_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render_to_response('book.html', locals(), context_instance=RequestContext(request))
