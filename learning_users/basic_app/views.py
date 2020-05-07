from django.shortcuts import render

from basic_app.forms import UserForm, UserProfileInfoForm

#imports
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)# set the html formpage variable as an actual form
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()# final model save

        #Extra info, website link & profile picture
            profile = profile_form.save(commit=False)# get data from html form template variable 'profile_form',commit=False don't save yet
            profile.user = user

            if 'picture_profile' in request.FILES:
                profile.picture_profile = request.FILES['picture_profile']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


#The login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {}, Password:{}".format(username, password))
            return HttpResponse("Invalid login details Supplied")
    else:
        return render(request,'basic_app/login.html', {})

#The logout view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

#A special view
@login_required
def special(request):
    return render(request, 'basic_app/special.html')
