from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            # Generate and return a token (if needed) or any other user-related data
            # For simplicity, we're returning a JSON response with a success message.
            return JsonResponse({'message': 'Login successful'})
        else:
            # Handle login error here and return an appropriate response.
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

    # Return an error response for non-POST requests.
    return JsonResponse({'error': 'Invalid request method'}, status=400)

