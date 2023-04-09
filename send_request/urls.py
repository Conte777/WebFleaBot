from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:model_id>', views.create_edit_sendmodel, name='sending_model'),
]
