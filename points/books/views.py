from django.shortcuts import render, redirect
from .models import Book
from django import forms


# Create your views here.
# load the index.html
def open_home_page(request):
    return render(request, "base.html")


# Search books
def search_books(request):
    return render(request, "search_books.html")


# login page
def open_login_page(request):
    return render(request, "login.html")
