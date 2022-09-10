from cProfile import label
from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields, models
from .models import AuthenticateUser, Books, BookManager
import datetime

class AuthSignUpForm(forms.ModelForm):
    class Meta:
        roleChoice = [
            ('LIBRARIAN', 'LIBRARIAN'),
            ('MEMBER', 'MEMBER')
            ]

        model = AuthenticateUser
        fields = ('username', 'password', 'role')
        label = {
            'username':'Username',
            'password':'Password',
            'role':'Role'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Password', 'type':'password'}),
            'role': forms.Select(choices=roleChoice, attrs={'class': 'form-control'})
        }

class AuthLoginForm(forms.ModelForm):
    class Meta:
        model = AuthenticateUser
        fields = ('username', 'password')
        label = {
            'username':'Username',
            'password':'Password'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Password', 'type':'password'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        available = [
            ('LIBRARIAN', 'LIBRARIAN'),
            ('MEMBER', 'MEMBER')
            ]

        model = Books
        fields = ('bookname', 'bookAvailable', 'bookPdf')
        label = {
            'bookname' : 'Book Name',
            'bookAvailable': 'Availability',
            'bookPdf': 'Book Pdf'
        }
        widgets = {
            'bookname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Name of the Book'}),
            'bookAvailable': forms.Select(choices=available, attrs={'class': 'form-control'}),
            'bookPdf': forms.FileInput(attrs={'class': 'form-control'})
        }

class BooksManagerForm(forms.ModelForm):
    class Meta:
        model = BookManager
        fields = ('username', 'bookID')
        label = {
            'username' : 'username',
            'bookID': 'Book ID'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'bookID': forms.TextInput(attrs={'class': 'form-control'})
        }