from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreationForm


@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("profile")
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        return super().form_valid(form)
