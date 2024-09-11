from django.contrib import admin
from django.urls import path

from . import views


urlpatterns =[
    path('admin/', admin.site.urls),
    path ('', views.home_view),
    path('login.html/', views.login_view),
    path('profil.html/', views.profil_view),
    ]