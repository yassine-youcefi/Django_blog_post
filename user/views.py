from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account is create successfuly for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'templates/sign_up.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'templates/profile.html')
