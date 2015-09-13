from django.shortcuts import render_to_response
from .models import Book
from django.shortcuts import RequestContext, get_object_or_404

# Create your views here.

def home(request):
    books = Book.objects.all().order_by('?')[:12]
    recent_books = Book.objects.all().order_by('-date')[:8]
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def itbook_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render_to_response('book.html', locals(), context_instance=RequestContext(request))