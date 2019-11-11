from django.shortcuts import render, HttpResponse, redirect
from .models import *


# ***********BOOK SECTION*************

def index(request):
    context= {
        "all_the_books": Books.objects.all()
    }
    return render(request, "index.html", context)

def add_book(request):
    print("Someone added a book")
    Books.objects.create(title=request.POST['title'], desc=request.POST['description'])
    return redirect("/")


def books(request, book_id):
    context = {
        'book': Books.objects.get(id=book_id),
        'all_authors': Authors.objects.all()
    }

    return render(request, "book.html", context)

def add_author_to_book(request):
    print(request.POST) # author_id & book_id
    author = Authors.objects.get(id=request.POST['author_id'])
    book = Books.objects.get(id=request.POST['book_id'])
    # add author to book
    book.author.add(author)
    return redirect(f"/books/{request.POST['book_id']}")

# ***********AUTHOR SECTION*************

def authors(request):
    context= {
        "all_the_authors": Authors.objects.all()
    }
    return render(request, "authors.html", context)

def add_author(request):
    print("Someone added an author")
    Authors.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect("/authors")

def author_page(request, author_id):
    context = {
        'author': Authors.objects.get(id=author_id),
        'all_books': Books.objects.all()
    }

    return render(request, "author_page.html", context)

def add_book_to_author(request):
    print(request.POST) # author_id & book_id
    author = Authors.objects.get(id=request.POST['author_id'])
    book = Books.objects.get(id=request.POST['book_id'])
    # add book to author
    author.book.add(book)
    return redirect(f"/author_page/{request.POST['author_id']}")