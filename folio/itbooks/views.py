from django.shortcuts import render_to_response
from .models import Book
from django.shortcuts import RequestContext
# Create your views here.

def home(request):
    books = Book.objects.all().order_by('?')[:12]
    recent_books = Book.objects.all().order_by('-date')[:8]
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))