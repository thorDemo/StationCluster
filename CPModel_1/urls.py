from django.urls import path, re_path
from . import views

app_name = 'Model1'

urlpatterns = [
    path('', views.index_page),
]
