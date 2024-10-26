
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm


# Create your views here.
def Home(request):
    return render(request,"inicio.html")

def StarLogin(request):
    formlogin=CustomAuthenticationForm()
    return render(request,"registration/sign-in.html",{"formlogin":formlogin})

@login_required
def MyProfile(request,):
    return render(request,'My_Profile/myprofile.html')


def login_view(request):
    if request.method == 'POST':
        formlogin = CustomAuthenticationForm(request, data=request.POST)
        if formlogin.is_valid():
            username = formlogin.cleaned_data.get('username')
            password = formlogin.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('MyProfile')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        formlogin = CustomAuthenticationForm()
    return render(request, 'registration/sign-in.html', {'formlogin': formlogin})



def Logout(request):
    formlogin = CustomAuthenticationForm()
    logout(request) 
    messages.error(request, 'Sesión concluida.')
    return render(request,'inicio.html')


def Login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,"dashboard.html")
    else :
        return render(request,'registration/login.html')