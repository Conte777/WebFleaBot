from django.http import HttpRequest
from django.shortcuts import render
from accounts.forms import ToggleSendForm
from send_request.models import SendModel

def index(request: HttpRequest):
    context = {"data": None, "form": None}
    if request.user.is_authenticated:
        context["data"] = request.user.sendmodel_set.all().values()
        context["form"] = ToggleSendForm(instance=request.user)
    return render(request, "main/home.html", context=context)

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