from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import userData

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success_page')  # Redirect to a success page
    else:
        form = UserForm()

    return render(request, 'create_user.html', {'form': form})

# def redirection(request):





def Home(request,*args, **kwargs):

        return HttpResponse("<h1> Hello World </h1>")

def About(request,*args, **kwargs):

        return HttpResponse("<h1> About Section </h1>")

def Link(request,*args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        print(request.user)
        return HttpResponse("<h1> Link </h1>")

def fn_without_req(*args, **kwargs):
        return HttpResponse("<p> MHeeee </p>")


def another(request):
        return render(request, "abc.html", {})

def home(request):
        my_dict = {
                "1st_key": "WABALABA DUBDUBBBB!!!!!!",
                "2nd_one": "Family ties, Kendric lamar.",
                "3rd": "<h1> a header </h1>",

        }
        return render(request, "abc.html", my_dict)

def about(request):
        return render(request, "about.html", {})

def contacts(request):
        return render(request, "contacts.html", {})

def services(request):
        return render(request, "services.html", {})

# Create your views here.

