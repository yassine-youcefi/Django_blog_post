from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def sign_up(request):
    if request.method == 'POST':    
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is create successfuly for {username}')
            return redirect('index')
    else:
            form = UserCreationForm()
    return render(request, 'templates/sign_up.html', {'form':form})

 