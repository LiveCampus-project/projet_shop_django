from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import SignUpForm, UserForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = False 
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def user_detail(request, user_id):
    return render(request, 'accounts/account_detail.html', {'user_id': user_id})

@login_required
def user_update(request, user_id):
    if request.method == 'POST':
        form = UserForm(request.POST, instance=User)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user_id)
    else:
        form = UserForm(instance=user_id)
    return render(request, 'factures/facture_form.html', {'form': form})