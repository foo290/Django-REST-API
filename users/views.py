from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.


def register_user(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}, You can login with these credentials now!')
            return redirect('Log-In')
    else:
        form = UserRegisterForm()

    return render(request, 'loginsys/signup_page.html', context={'form': form})



@login_required()
def profile(request):
    return render(request, 'users/profile.html')
