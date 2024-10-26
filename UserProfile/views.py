from django.shortcuts import render

# Create your views here.
def List_Profiles(request):
    return render(request,"User_Profile/list_users_profiles.html")

def View_Profile(request):
    return render(request,"User_Profile/view_profile.html")

def Login(request):
    pass