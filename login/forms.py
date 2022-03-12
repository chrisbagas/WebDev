from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=60)

    class Meta:
        model = Account
        fields = ('full_name','username','password1','password2')