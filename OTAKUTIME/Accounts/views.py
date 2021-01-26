from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.views import generic



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request,user)

            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'Accounts/signup.html',{'form':form})


def editprofile_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request,user)

            return redirect('home')
    else:
        form = UserChangeForm()
    
    return render(request, 'Accounts/edit_profile.html',{'form':form})
    
    def get_object(self):
        self.request.user


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request,user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render (request, 'Accounts/login.html',{'form':form})



def logout_view(request):
    if request.method == 'POST':
        logout(request)

        return redirect('home')


def profile_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request,user)
    else:
        form = AuthenticationForm()
    return render (request, 'Accounts/profile.html',{'form':form})

    