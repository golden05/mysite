from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def search(request):
    """docstring for search"""
    error = False
    if 'q' in request.GET: 
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_results.html', {'books': books,'length': books.count(), 'query': q})
    render(request, 'books/search_form.html', {'error':error})
