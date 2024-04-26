from django.shortcuts import render
from users.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        
        if User.objects.filter(email=email).exists() or User.objects.filter(phone_number=phone_number).exists():
            messages.error('User is already registered')
        else:
            user = User.objects.create(
                first_name=first_name, last_name=last_name, phone_number=phone_number, email=email
            )
            user.save()

            if not UserData.objects.filter(user=user).exists():
                UserData.objects.create(user=user)
                login(request, user)


    return render(request, 'signup.html')