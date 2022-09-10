from django.contrib import admin
from .models import *

class AuthenticateUserAdmin(admin.ModelAdmin):
    list_display= ['username','password','role']

class BooksAdmin(admin.ModelAdmin):
    list_display= ['bookname', 'bookAvailable', 'bookPdf', 'bookID']

class BookManagerAdmin(admin.ModelAdmin):
    list_display= ['username', 'bookID']


admin.site.register(AuthenticateUser, AuthenticateUserAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(BookManager, BookManagerAdmin)