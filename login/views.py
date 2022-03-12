from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .forms import SignUpForm

# Create your views here.

def signupPage(request):
    # if request.user.is_authenticated:
    #     return redirect('index')
    # else:
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            password = form.cleaned_data.get('password1')
            account = authenticate(full_name = full_name, password = password)
            login(request,account)
            # messages.success(request, 'Akun telah dibuat dengan username ' + user + ". Silakan login.")
            # return redirect('login')
    context = {'form': form}
    return render(request, 'signup.html', context)


# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user )
#                 return redirect('index')
#             else:
#                 messages.info(request, 'username atau password salah. ')
#         context = {}
#         return render(request, 'login.html', context)

# @login_required
# def logout(request):
#     django_logout(request)
#     return redirect('login')

