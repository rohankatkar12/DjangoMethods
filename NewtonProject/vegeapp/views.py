from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os
import re


# Create your views here.
def login_page(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect("/reciepe/login/")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/reciepe/login/")
        else:
            login(request, user)
            return redirect('/reciepe/showreciepe/')

    return render(request, "reciepe/login.html")


def logout_page(request):
    logout(request)
    return redirect("/reciepe/login/")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already taken....")
            return redirect("/reciepe/register/")
        
        if len(password) < 6:
            messages.error(request, "Password must be atleast 6 characters....")
            return redirect("/reciepe/register/")
        
        # Email Validation using regular expression--->
        # if not re.match(r'^.+@[^.].*\.[a-z]{2,10}$', email):
        #     messages.info(request, "Invalid Email")
        #     return redirect("/reciepe/register/")
        
        form = EmailForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username
            )
            user.set_password(password)
            user.is_staff = True
            user.save()
        else:
            messages.error(request, "Invalid Email....")
            return redirect("/reciepe/register/")

        return redirect('/reciepe/register/')

    return render(request, "reciepe/register.html")


@login_required(login_url="/reciepe/login/")
def addreceipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect('/reciepe/showreciepe/')
    
    return render(request, 'reciepe/index.html', context={'page':'Reciepe Form'})


@login_required(login_url="/reciepe/login/")
def showreciepe(request):
    page = "Reciepe List"
    receipes = Receipe.objects.all().order_by('-created_at')
    # obj = receipes.reverse()
    print(receipes)
    
    if request.GET.get('search'):
        print(request.GET.get('search'))
        receipes = receipes.filter(receipe_name__icontains = request.GET.get('search'))

    return render(request, 'reciepe/reciepes.html', context={'receipes':receipes, 'page':page})


@login_required(login_url="/reciepe/login/")
def deletereciepe(request, id):
    receipes = Receipe.objects.get(id=id)

    image_path = os.path.join(settings.MEDIA_ROOT, f"{receipes.receipe_image}")
    if os.path.exists(image_path):
        os.remove(image_path)
    receipes.delete()

    return redirect('showreciepe')


@login_required(login_url="/reciepe/login/")
def editreciepe(request, id):
    if request.method == "POST":
        obj = Receipe.objects.get(id=id)

        if request.POST['receipe_name']:
            obj.receipe_name = request.POST['receipe_name']

        if request.POST['receipe_description']:
            obj.receipe_description = request.POST['receipe_description']

        if request.FILES.get('receipe_image'):
            image_path = os.path.join(settings.MEDIA_ROOT, f"{obj.receipe_image}")
            if os.path.exists(image_path):
                os.remove(image_path)
            obj.receipe_image = request.FILES['receipe_image']
        
        obj.save()
        return redirect('showreciepe')
           

    receipes = Receipe.objects.get(id=id)
    page = "Edit Reciepe"
    return render(request, 'reciepe/edit.html', context={'receipes':receipes, 'page':page})

