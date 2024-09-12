from django.contrib import admin
from django.urls import path

from . import views


urlpatterns =[
    path('admin/', admin.site.urls),
    path ('', views.home_view),
    path('login/', views.login_view),
    path('profil/', views.profil_view),
    path('sigup/', views.sigup_view),
]