# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    data = {
        "contacts": {
            "Discord": "Conte#8928",
            "Telegram": "@Koleso7777",
            "VK": "@koleso777",
            "Телефон": "+79153298361",
        },
    }
    return render(request, "main/contact.html", context=data)