from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    return render(request, 'accounts/register.html', {'form':form})

def profile(request):
    return render(request, 'accounts/general.html')


def home(request):
    return render(request,'accounts/dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        print(user)
        login(request, user)
        
        # login hoye geche
        
        return redirect('home')
    return render(request, 'accounts/signin.html')

