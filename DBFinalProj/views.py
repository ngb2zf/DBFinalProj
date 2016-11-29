from django.db import connection
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from bandsapp.models import Hosts, Bands, Events
from django.contrib.auth.decorators import login_required
from .forms import MyRegistrationForm, Band_MyRegistrationForm, Host_MyRegistrationForm, Event_MyRegistrationForm
# Create your views here.

#temporary
event_summary = 0

@login_required(login_url='/accounts/not_loggedin/')
def index(request):
    # This code will be in each view where we need to tell user or host
    # , it's how we are distinguising between hosts and bands
    hosts_list = Hosts.objects.all()
    bands_list = Bands.objects.all()

    user_id = request.user.id

    # True if you are host, False if you are a band
    user_Type = get_User_Type(user_id)


    # Code for host at index
    if user_Type:
        host_names = []
        for h in hosts_list:
            host_names.append(h.h_name)

        # Sets var band to the band object with the corresponding user_id
        host = 0
        for h in hosts_list:
            if h.user_id == user_id:
                host = h

        query = "select * from bandsapp_events where h_id_id = " + str(host.h_id) + ";"

        print(query)

        events = Events.objects.raw(query)

        return render_to_response('host_index.html',{"user": request.user,"host_names":host_names, "bands_list":bands_list, "host":host, "events":events})

    # Code for band at index
    elif user_Type == False:
        host_names = []
        for h in hosts_list:
            host_names.append(h.h_name)

        # Sets var band to the band object with the corresponding user_id
        band = 0
        for b in bands_list:
            if b.user_id == user_id:
                band = b


        return render_to_response('bands_index.html',{"user": request.user,"host_names":host_names, "bands_list":bands_list, "band":band})


def delete_event(request):
    query = "delete from bandsapp_events where e_id = " + str(request.GET['e_id']) + ";"

    print(query)

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    return HttpResponseRedirect('/accounts/event_delete_success')


def login(request):
    return render_to_response('login.html', {"user": request.user,})


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin',{"user": request.user,})
    else:
        return HttpResponseRedirect('/accounts/invalid')


@login_required(login_url='/accounts/not_loggedin/')
def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username,"user": request.user})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


#Not being used, will leave in for now
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
    auth.logout(request)
    if request.method == 'POST':

        form = Band_MyRegistrationForm(request.POST)
        form2 = MyRegistrationForm(request.POST)
        if form.is_valid() & form2.is_valid():
            user = form2.save()

            band = form.save(commit=False)
            band.user = user

            band.save()
            return HttpResponseRedirect('/accounts/register_success',{"user": request.user})

    else:
        form = Band_MyRegistrationForm()
        form2 = MyRegistrationForm()
    args = {}
    # args.update(csrf(request))

    args['form'] = form
    args['form2'] = form2

    return render_to_response('register_band.html', args)


@login_required(login_url='/accounts/not_loggedin/')
def edit_profile(request):
    bands_list = Bands.objects.all()

    user_id = request.user.id
    # Sets var band to the band object with the corresponding user_id
    band = 0
    for b in bands_list:
        if b.user_id == user_id:
            band = b

    my_record = band
    if request.method == 'POST':
            form = Band_MyRegistrationForm(request.POST, instance=my_record)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/',{"user": request.user})
    else:
        my_record = band
        form = Band_MyRegistrationForm(instance=my_record)

    return render_to_response('edit_profile.html',{"band":band, "user":request.user, "form":form})

@login_required(login_url='/accounts/not_loggedin/')
def host_edit_profile(request):
    hosts_list = Hosts.objects.all()

    user_id = request.user.id
    # Sets var band to the band object with the corresponding user_id
    host = 0
    for h in hosts_list:
        if h.user_id == user_id:
            host = h

    my_record = host
    if request.method == 'POST':
            form = Host_MyRegistrationForm(request.POST, instance=my_record)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/',{"user": request.user})
    else:
        my_record = host
        form = Host_MyRegistrationForm(instance=my_record)

    return render_to_response('host_edit_profile.html',{"host":host, "user":request.user, "form":form})


def register_host(request):
    auth.logout(request)
    if request.method == 'POST':

        form = Host_MyRegistrationForm(request.POST)
        form2 = MyRegistrationForm(request.POST)
        if form.is_valid() & form2.is_valid():
            user = form2.save()

            host = form.save(commit=False)
            host.user = user

            host.save()
            return HttpResponseRedirect('/accounts/register_success',{"user": request.user})

    else:
        form = Host_MyRegistrationForm()
        form2 = MyRegistrationForm()
    args = {}
    # args.update(csrf(request))

    args['form'] = form
    args['form2'] = form2

    return render_to_response('register_host.html', args)


@login_required(login_url='/accounts/not_loggedin/')
def register_event(request):
    if request.method == 'POST':

        form = Event_MyRegistrationForm(request.POST)
        if form.is_valid():
            event = form.save(commit = False)
            hosts_list = Hosts.objects.all()
            user_id = request.user.id
            host = 0
            for h in hosts_list:
                if h.user_id == user_id:
                    host = h
            event.h_id_id = host.h_id
            event.save()

            set_event_summary(event)

            return HttpResponseRedirect('/accounts/register_event_success',{"user":request.user})

    else:
        form = Event_MyRegistrationForm()

    args = {}

    args['form'] = form
    args['user'] = request.user

    return render_to_response('register_event.html', args)

def set_event_summary(event):
    global event_summary
    event_summary = event

def get_event_summary():
    global event_summary
    return event_summary



@login_required(login_url='/accounts/not_loggedin/')
def register_event_success(request):
    event = get_event_summary()
    return render_to_response('register_event_success.html',{"user": request.user,"event":event})

def event_delete_success(request):
    return render_to_response('event_delete_success.html',{"user": request.user,})


def register_success(request):
    return render_to_response('register_success.html',{"user": request.user,})


def get_User_Type(user_id):
    # Return True if user is a Host
    # Return False if user is a Band
    hosts_list = Hosts.objects.all()
    bands_list = Bands.objects.all()

    host = 0
    for h in hosts_list:
        if h.user_id == user_id:
            host = h

    band = 0
    for b in bands_list:
        if b.user_id == user_id:
            band = b

    if band == 0:
        return True
    elif host == 0:
        return False


@login_required(login_url='/accounts/not_loggedin/')
def profile(request):
    hosts_list = Hosts.objects.all()
    bands_list = Bands.objects.all()

    user_id = request.user.id

    host = 0
    for h in hosts_list:
        if h.user_id == user_id:
            host = h

    band = 0
    for b in bands_list:
        if b.user_id == user_id:
            band = b

    user_Type = get_User_Type(user_id)

    return render_to_response('profile_test.html',{"user": request.user,"user_id":user_id, "host":host, "band":band, "user_Type":user_Type})


def not_loggedin(request):
     return render_to_response('not_loggedin.html')




