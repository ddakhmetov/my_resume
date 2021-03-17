from django.urls import path
from .views import Register, user_login, user_logout, cabinet

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('cabinet/', cabinet, name='cabinet'),
]