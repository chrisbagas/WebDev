from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.http import JsonResponse
from .forms import SignUpForm

# Create your views here.

def signupPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Akun telah dibuat dengan username ' + username + ". Silakan login.")
            return redirect('login_acc')
    context = {'form': form}
    return render(request, 'signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user )
                return redirect('index')
            else:
                messages.info(request, 'username atau password salah. ')
        context = {}
        return render(request, 'login.html', context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')

