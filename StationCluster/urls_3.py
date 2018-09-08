from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include("CPModel_3.urls")),
    path('admin/', admin.site.urls),
]