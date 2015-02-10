from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.decorators import login_required

from auth.forms import UserProfileForm, UserForm


def register(request):
    registered = False  # will set to True when registration is successful

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, "auth/register.html", {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    })


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            dj_login(request, user)
            return HttpResponseRedirect('/rango/')
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'auth/login.html', {'error': username})
    else:
        return render(request, 'auth/login.html', {})


@login_required
def logout(request):
    dj_logout(request)
    return HttpResponseRedirect('/rango/')



