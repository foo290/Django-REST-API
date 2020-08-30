from django.shortcuts import (
    render,
    redirect   
)


# Create your views here.

def login_page(request):
    
    return render(request, 'loginsys/login_page.html')



