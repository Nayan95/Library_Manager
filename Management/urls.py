from django.contrib import admin
from django.urls import path
from .views import *

app_name = "Management"

urlpatterns = [
    path('', login),
    path('signup/', signup),
    path('home/<username>', homePage),
    path('updateBook/<username>', updateBook),
    path('updateBookName/<username>/<bookID>', updateBookName),
    path('deleteBook/<bookID>/<username>', deleteBook),
    path('borrow/<username>', borrowBooks)
]