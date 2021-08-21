from django.urls import path
from . import views

app_name = 'resume_builder'

urlpatterns = [
    path('', views.index, name='index'),
]
