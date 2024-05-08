from django.shortcuts import render
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from accounts.models import ContactMessage


# Create your views here.
# load the index.html
def open_home_page(request):
    return render(request, "base.html")


def search_books(request):
    if request.method == "POST":
        name = request.POST.get("name_of_book")  # Get the name from the form submission
        books = Book.objects.filter(title__icontains=name)  # Search the database
        return render(
            request, "search_books.html", {"books": books}
        )  # Render the results to search_books.html
    else:
        books = Book.objects.all()  # Retrieve all books from the database
        if request.user.is_authenticated:
            return render(
                request, "search_books.html", {"books": books, "authenticated": True}
            )
        else:
            return render(
                request, "search_books.html", {"books": books, "authenticated": True}
            )


# login page
def open_login_page(request):
    return render(request, "login.html")


# forgot_password
@csrf_exempt  # Disable CSRF protection for this view (for demonstration purposes only)
def get_inquiries_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Create a new ContactMessage object and save it to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Optionally, you can redirect the user to a thank you page or display a success message
        return render(request, "thank_you.html")
    else:
        return render(request, "base.html#about-us")
