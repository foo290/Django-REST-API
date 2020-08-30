from django.shortcuts import (
    render,
    redirect   
)

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.

def login_page(request):
    
    return render(request, 'loginsys/login_page.html')


def register_user(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'loginsys/signup_page.html', context={'form': form})
