from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect('reciepes/')
    
    receipes = Receipe.objects.all()
        
    return render(request, 'reciepe/index.html', context={'receipes':receipes})