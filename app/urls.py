from django.urls import path
from .views import registro_usuario
from . import views

urlpatterns = [
    path('accounts/login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('registro/', registro_usuario, name='registro_usuario'),
]