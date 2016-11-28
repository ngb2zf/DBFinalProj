from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .forms import MyRegistrationForm, Band_MyRegistrationForm, Host_MyRegistrationForm
# Create your views here.


def index(request):
    return render_to_response('index.html')


def login(request):
    c = {}
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    else:
        form = MyRegistrationForm()
    args = {}
    # args.update(csrf(request))

    args['form'] = form

    return render_to_response('register.html', args)

def register_band(request):
    if request.method == 'POST':

        form = Band_MyRegistrationForm(request.POST)
        form2 = MyRegistrationForm(request.POST)
        if form.is_valid() & form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect('/accounts/register_success')

    else:
        form = Band_MyRegistrationForm()
        form2 = MyRegistrationForm()
    args = {}
    # args.update(csrf(request))

    args['form'] = form
    args['form2'] = form2

    return render_to_response('register_band.html', args)


def register_host(request):
    if request.method == 'POST':

        form = Host_MyRegistrationForm(request.POST)
        form2 = MyRegistrationForm(request.POST)
        if form.is_valid() & form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect('/accounts/register_success')

    else:
        form = Host_MyRegistrationForm()
        form2 = MyRegistrationForm()
    args = {}
    # args.update(csrf(request))

    args['form'] = form
    args['form2'] = form2

    return render_to_response('register_host.html', args)


def register_success(request):
    return render_to_response('register_success.html')

