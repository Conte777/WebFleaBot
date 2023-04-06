# from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from accounts.models import SendModel

def index(request: HttpRequest):
    # print(SendModel.objects.filter(user=request.user))
    data = {"data": []}
    if request.user.is_authenticated:
        data["data"] = request.user.sendmodel_set.all().values()
    return render(request, "main/home.html", context=data)

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