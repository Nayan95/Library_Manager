from multiprocessing import context
from webbrowser import get
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import AuthenticateUser, Books, BookManager
from .forms import *

userlogin = False

def login(request):
    global userlogin
    userlogin = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if "login" in request.POST:
            try:
                user = AuthenticateUser.objects.get(username = username)
            except:
                messages.warning(request, 'User not found.')
                return redirect('/')
            
            if (user.password == password):
                userlogin = True
                return redirect('/home/{}'.format(username))
            else:
                messages.warning(request, 'Invalid Password!')
                return redirect('/')
        elif "signup" in request.POST:
            return redirect('/signup/')
    
    return render(request, "login.html")

def signup(request):
    global userlogin
    signupForm = AuthSignUpForm()
    if request.method == 'POST':
        print('Receiving a post request')
        if "register" in request.POST:
            print('Receiving a register request')
            signupForm = AuthSignUpForm(request.POST)
            if signupForm.is_valid():
                print('Receiving a valid request')
                regForm = AuthSignUpForm({
                    'username': signupForm.cleaned_data['username'],
                    'password': signupForm.cleaned_data['password'],
                    'role': signupForm.cleaned_data['role']
                })
                regForm.save()
                userlogin = True
                messages.success(request, 'Registeration Successful!')
                return redirect('/home/{}'.format(signupForm.cleaned_data['username']))
            else:
                messages.warning(request, 'Username already used!')
        
        elif "login" in request.POST:
            return redirect('/')
    context = {
        "signupForm" : signupForm
    }
    return render (request, "signup.html", context)

def homePage(request,username):
    addBook = BookForm()
    userRole = AuthenticateUser.objects.filter(username=username).values_list('role', flat=True)
    print(userRole[0])
    getBorrowedBooks = BookManager.objects.filter(username=username).values_list('bookID', flat=True)
    bookname = Books.objects.filter(bookID__in = getBorrowedBooks)

    if request.method == 'POST':
        if "create" in request.POST:
            addBook = BookForm(request.POST, request.FILES)
            if addBook.is_valid():
                addBook.save()
                messages.success(request, 'Book Added Successfully')
        
        elif "borrow" in request.POST:
            return redirect('/borrow/{}'.format(username))

        elif "return" in request.POST:
            bookID = request.POST.get('return')
            returnBook = BookManager.objects.all().filter(bookID=bookID)
            returnBook.delete()

            getBook = Books.objects.get(bookID = bookID)
            getBook.bookAvailable = 'True'
            getBook.save()
            return redirect('/home/{}'.format(username))

        elif "logout" in request.POST:
            return redirect('/')
        
        elif "deleteacc" in request.POST:
            returnBook = BookManager.objects.all().filter(username=username)
            if not returnBook:
                getUser = AuthenticateUser.objects.get(username = username)
                getUser.delete()
                return redirect('/')
            else:
                messages.warning(request, "Please return all your borrowed books first")

    context = {
        "userRole":userRole[0],
        "userlogin":userlogin,
        "bookname": bookname,
        "addBook": addBook,
        "username":username
    }
    return render (request, "home.html", context)

def updateBook(request, username):
    allBooks = Books.objects.all()
    
    context = {
        "books":allBooks,
        "username":username,
        "userlogin":userlogin
    }
    return render(request, "update.html", context)

def updateBookName(request, username, bookID):
    getBook = Books.objects.get(bookID=bookID)
    updateBook = BookForm(request.POST or None, request.FILES or None, instance=getBook)
    if updateBook.is_valid():
        updateBook.save()
        return redirect('/updateBook/{}'.format(username))
    
    context = {
        'getBook': getBook,
        'updateBook': updateBook,
        'username': username,
        'userlogin': userlogin
    }
    return render(request, 'updateBookDetails.html', context)

def deleteBook(request, bookID, username):
    print("in delete " + bookID)
    getBook = Books.objects.get(bookID=bookID)
    getBook.delete()
    return redirect('updateBook/{}'.format(username))

def borrowBooks(request, username):
    getAvailableBook = Books.objects.filter(bookAvailable='True')
    if request.method == 'POST':
        print("POST")
        if 'choose' in request.POST:
            print("CHOSOE")
            val = request.POST.get('choose')
            addBk = BooksManagerForm({
                'username':AuthenticateUser.objects.get(username=username),
                'bookID': Books.objects.get(bookID = val)
            })
            addBk.save()
            messages.success(request, 'Book Added!')

            getBook = Books.objects.get(bookID = val)
            getBook.bookAvailable = 'False'
            getBook.save()
            return redirect('/home/{}'.format(username))
            
            
    context = {
        'books':getAvailableBook,
        'username':username,
        'userlogin':userlogin
    }
    return render(request, "borrowBook.html", context)
