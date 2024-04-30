from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('signup/', signup, name='register'),
    path('login/', login, name='login')
]