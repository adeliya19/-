from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserChangeForm):
    class Meta:
        models = User
        fields = ['username','password1','password2']
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

