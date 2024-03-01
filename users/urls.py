from django.urls import path
from .views import landing, login, register


urlpatterns = [
    path('landing/', landing, name="landing"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]