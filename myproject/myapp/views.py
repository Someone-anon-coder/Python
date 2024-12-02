# Import the HttpResponse class from Django's http module
from django.http import HttpResponse

# Define a view function named 'home' that takes a request object as an argument
def home(request):
    # Return an HTTP response with the string "Hello, Django!"
    return HttpResponse("Hello, Django!")