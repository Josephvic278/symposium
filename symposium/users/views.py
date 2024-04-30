from django.shortcuts import render
from django.http import JsonResponse
from users.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def signup(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        username = random.choice(string.ascii_letters)
        if User.objects.filter(email=email).exists() or User.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'message':'User has already been registered','status':'fail'})
        else:
            user = User.objects.create(
                first_name=first_name, last_name=last_name, phone_number=phone_number, email=email,username = username
            )
            user.save()

            if not UserData.objects.filter(user=user).exists():
                UserData.objects.create(user=user)
                return JsonResponse({'message':'You have successfully registered', 'status':'success'})

    return render(request, 'signup.html')

def login(request):
    users = User.objects.all()
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        phone_number = data.get('phone_number')

        if email == 'mainadmin@gmail.com':
            user = User.objects.filter(phone_number=phone_number, email=email)
            if user is not None:
                return JsonResponse({'message':'Welcome Admin', 'status':'success'})
            else:
                print(False)
        else:
            return JsonResponse({'message':'User is not an admin', 'status':'fail'})
    return render(request, 'login.html')