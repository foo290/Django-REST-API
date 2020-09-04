from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def home(request):
    print(request.body)
    print(request.method)
    return render(request, 'homepage/home.html')