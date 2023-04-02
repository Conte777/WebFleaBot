from django.urls import include, path
from . import views

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("profile/", views.profile_view, name="profile"),
    path("registration/", views.RegisterView.as_view(), name="register")
]
