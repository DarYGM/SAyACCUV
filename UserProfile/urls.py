from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from .views import List_Profiles,View_Profile
from App.views import MyProfile


urlpatterns = [
    path('list',List_Profiles,name="List_Profiles"),
    path('view-profile',View_Profile,name="View_Profile"),
    path('my-profile',MyProfile,name="MyProfile"),
    
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)