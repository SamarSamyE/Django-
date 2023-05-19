from django import views
from django.urls import path
from .views import index,show,delete,update
app_name = 'books'
urlpatterns = [
    path('books', index,name="books-index"),
    path('books/<int:id>', show,name="books-show"),
    path('books/<int:id>/delete', delete,name="books-delete"),
    path('books/<int:id>/update', update,name="books-update"),
]
