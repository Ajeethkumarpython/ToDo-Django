from django.shortcuts import render, HttpResponse, redirect
from .models import Tasks
from .forms import Task_form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def insert_task(request):
    form = Task_form()
    tasks = Tasks.objects.all()
    if request.method == 'POST':
        form = Task_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'home.html', {'form':form, 'tasks':tasks})

def delete_task(request, pk):
    tasks = Tasks.objects.get(pk=pk)
    tasks.delete()
    return redirect('home')

def update_task(request, pk):
    task = Tasks.objects.get(pk=pk)
    form = Task_form(request.POST, instance=task)
    if form.is_valid():
        form.save(commit=True)
        return redirect('home')
    return render(request, 'update.html', {'task':task})

#User registration and login

def user_register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successfull")
            return redirect('home')
        messages.error(request, "Unsuccessfull Registration. Invalid information")
    form=UserCreationForm()
    return render(request,'auth/sign_up.html',{"form":form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Welcome {username}.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form=AuthenticationForm()
    return render(request, 'auth/login.html',{"form":form})