from django.contrib.auth import authenticate , login , get_user_model
from django.shortcuts import render , redirect
from django.http import Http404, HttpResponse
from .forms import ContactForm , LoginForm , RegisterForm


#creating homepage
def home_page(request):
    context = {
        'message': 'Hello welcome back'
    }  #for passing the files or messages to html files
    return render(request, 'home_page.html', context)


def about_us_page(request):
    context = {
        'about': 'hello this is us since 1404 , from about us function'
    }

    return render(request, 'about_us_page.html', context)


def contact_us_page(request):
    contact_form = ContactForm()
    #for seeing what user has sent us
    if request.method == "POST":
        print(request.POST.get('fullName'))
        print(request.POST.get('email'))
        print(request.POST.get('message'))


    # for sending infos to user
    context = {
        'contact': 'this is the contact page you all',
        'contact_form': contact_form
    }
    return render(request,'contact_us_page.html',context)

def login_page(request):
    print(request.user.is_authenticated)
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        userName = login_form.cleaned_data.get('userName')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request,username=userName, password=password)#red ones are data base
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print('Login failed')

    context = {
        'logmessage': 'hello this is our login page',
        'login_form': login_form
    }

    return render(request, 'auth/login.html', context)


user = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        userName = register_form.cleaned_data.get('userName')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        user.objects.create_user(username=userName, email=email, password=password)#query set default by django

    context = {
        'title': 'Register Page',
        'message': 'hello this is our register page',
        'register_form':register_form

    }


    return render(request,'auth/register.html',context)



