from django.shortcuts import render, reverse, HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from UserApp.forms import LoginForm, RegesterForm
from UserApp.models import SomeUser

# Create your views here.
def regesterview(request):
    if request.method == 'POST':
        form = RegesterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newUser = SomeUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name = data['display_name']
            )
        newUser.save()
    form = RegesterForm()
    html = 'regester.html'
    return render(request, html, {'form': form})

@login_required
def index(request):
    return render(request, 'index.html')


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()
    html = 'login.html'
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))