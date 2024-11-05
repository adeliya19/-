from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate
def index(request):
    '''
    Домашняя страница
    '''
    return render(request,'index.html') 

def signup(request):
    '''
    Страница регистрации
    '''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
         form = SignupForm()
    return render(request, 'signup.html', {'form':form})

def login(request):
    '''
    Страница входа в личный кабинет
    '''
    if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.changed_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request,user)
                    return redirect ('home')
    else:
         form = LoginForm()
    return render(request,'login.html', {'form':form})


                     