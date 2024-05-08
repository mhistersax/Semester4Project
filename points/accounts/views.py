from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def verify_users_credentials(request):
    # Get the username and password from the request parameters
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")
        # Check if both username and password are provided
        if not (username and password):
            return JsonResponse(
                {"error": "Both username and password are required"}, status=400
            )

        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            # User with the provided credentials exists
            return JsonResponse({"valid": True, "message": "Credentials are valid."})
        else:
            # User with the provided credentials does not exist
            return JsonResponse(
                {"valid": False, "message": "Invalid credentials."}, status=400
            )

    else:
        # Only GET requests are allowed
        return JsonResponse({"error": "Method not allowed"}, status=405)


# list all user
def list_users(request):
    if request.method == "GET":
        # Retrieve all users from the User model
        users = User.objects.all()

        # Serialize user data
        user_data = []
        for user in users:
            user_data.append(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    # Add more fields as needed
                }
            )

        # Return JSON response containing user data
        return JsonResponse({"users": user_data})

    else:
        # Only GET requests are allowed
        return JsonResponse({"error": "Method not allowed"}, status=405)


# sign up a user
@csrf_exempt  # Disable CSRF protection for this view (for demonstration purposes only)
def sign_up(request):
    if request.method == "POST":
        # Get the username and password from the request parameters
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if both username and password are provided
        if not (username and password):
            return JsonResponse(
                {"error": "Both username and password are required"}, status=400
            )

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username is already taken"}, status=400)

        # Create the user
        user = User.objects.create_user(username=username, password=password)

        # Optionally, you can perform additional actions here, such as sending a confirmation email

        # Return a success response
        return JsonResponse({"success": True, "message": "User created successfully"})

    else:
        # Only POST requests are allowed
        return JsonResponse({"error": "Method not allowed"}, status=405)


# forgot_password
@csrf_exempt  # Disable CSRF protection for this view (for demonstration purposes only)
def forgot_password(request):
    if request.method == "POST":
        # Get the username and new password from the request parameters
        username = request.POST.get("username")
        new_password = request.POST.get("new_password")

        # Check if both username and new password are provided
        if not (username and new_password):
            return JsonResponse(
                {"error": "Both username and new password are required"}, status=400
            )

        # Check if the user with the provided username exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=400)

        # Set the new password for the user
        user.set_password(new_password)
        user.save()

        # Optionally, you can perform additional actions here, such as sending a confirmation email

        # Return a success response
        return JsonResponse(
            {"success": True, "message": "Password updated successfully"}
        )

    else:
        # Only POST requests are allowed
        return JsonResponse({"error": "Method not allowed"}, status=405)
