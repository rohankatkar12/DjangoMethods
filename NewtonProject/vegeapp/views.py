from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import os

# Create your views here.

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

        return redirect('showreciepe')
    
    return render(request, 'reciepe/index.html', context={'page':'Reciepe Form'})


def showreciepe(request):
    page = "Reciepe List"
    receipes = Receipe.objects.all()
    # for rece in receipes:
    #     print(rece.receipe_image, type(rece.receipe_image))
    return render(request, 'reciepe/reciepes.html', context={'receipes':receipes, 'page':page})


def deletereciepe(request, id):
    receipes = Receipe.objects.get(id=id)

    image_path = os.path.join(settings.MEDIA_ROOT, f"{receipes.receipe_image}")
    if os.path.exists(image_path):
        os.remove(image_path)
    receipes.delete()

    return redirect('showreciepe')


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

