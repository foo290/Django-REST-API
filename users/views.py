from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
)


# Create your views here.


def register_user(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}, You can login with these credentials now!')
            return redirect('account_login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/signup_page.html', context={'form': form})




@login_required()
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()

            messages.success(request, f'Profile is updated!')
            return redirect('User-Profile')

    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)    

    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form,
    }

    return render(request, 'users/profile.html', context)
