from pickle import TRUE
from random import choice
from django.db import models
import uuid

roleChoice = [
    ('LIBRARIAN', 'LIBRARIAN'),
    ('MEMBER', 'MEMBER')
    ]
available = [
    ('True', 'True'),
    ('False', 'False')
]

class AuthenticateUser(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=15, choices=roleChoice, default='MEMBER')

    def __str__(self):
        return (self.username)

class Books(models.Model):
    bookname = models.CharField(max_length=200)
    bookAvailable = models.CharField(max_length=5, choices=available, default='True')
    bookID = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    bookPdf = models.FileField(upload_to='media/', null=True, max_length=200)

    def __str__(self):
        return (self.bookname)
    

class BookManager(models.Model):
    username = models.ForeignKey("AuthenticateUser", on_delete=models.CASCADE, null=True)
    bookID = models.ForeignKey("Books", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.bookID)
