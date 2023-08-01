from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    peoples = [
        {'name': 'Rohan Katkar', 'age': '22'},
        {'name': 'Atul Mharnur', 'age': '16'},
        {'name': 'Ashish Ranwalkar', 'age': '30'},
        {'name': 'Shriratna Ranwalkar', 'age':'26'},
        {'name': 'Amol Patil', 'age': '28'},
        {'name': 'Nikhil', 'age': '14'}
    ]

    text = """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        """
    vegetables = ['Pumpkin', 'Tomato', 'Potato', 'Broccoli', 'Cabbage', 'Carrot', 'Onion']
    Available_veg = ['Tomato', 'Potato', 'Carrot', 'Onion']
    
    return render(request, "firstapp/index.html", context = {'peoples': peoples, 'text':text, 'vegetables':vegetables, 'available_veg':Available_veg})


def contact(request):
    return render(request, 'firstapp/contact.html')


def about(request):
    return render(request, 'firstapp/about.html')


def success_page(request):
    return HttpResponse("<h1>Hey this is a success page</h1>")