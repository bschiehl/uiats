from django.urls import path

from . import views

urlpatterns = [
    path('', views.uiats_form, name='uiats_form'),
]