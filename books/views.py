from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


book_list = [{
        'index': 0,
        'id': 1,
        'name': 'Book1',
        'author': "amr abdelhamid",
        'description': "book 1 description",
        "price":100
    }, {
        'index': 1,
        'id': 2,
        'name': 'Book2',
        'author': "ahmed khaled tawfiq",
        'description': "book 2 description",
        "price":200
    },  {
        'index': 2,
        'id': 3,
        'name': 'Book3',
        'author': "Taha hussin",
        'description': "book 3 description",
        "price":300
    },]
# Create your views here.
def index(request):
    context = {'book_list': book_list}
    return render(request, 'index.html',context)

def show(request, id):
    book = _get_book(id)
    print(book)
    context = {'book': book}
    return render(request, 'show.html', context)


def delete(request, id):
    book = _get_book(id)
    if book:
        book_list.remove(book)
    return redirect("books:books-index")


def update(request,**kwargs):
    book=_get_book(kwargs.get('id'))
    if book:
        book['description']=f"price updated"
    return redirect("books:books-index")

def _get_book(id):
    for book in book_list:
        if book['id']==id:
            return book
    return None
