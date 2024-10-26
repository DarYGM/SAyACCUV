
from django.contrib import admin
from django.urls import path,include
from App.views import Home, StarLogin,Login,Logout
from django.contrib.auth.views import LoginView, LogoutView
from App.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home, name="Home"),
    path('login-in',login_view, name="login_view"),
    path('login/',Login,name="Login"),
    path('logout/',Logout,name="Logout"),
    path('user-profile/',include('UserProfile.urls')),

]
