from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from users.models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
import pandas as pd
import openpyxl
from io import BytesIO

def signup(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        username = random.choice(string.ascii_letters)
        registered_as = data.get('registered_as')
        faculty = data.get('faculty')
        department = data.get('department')

        if User.objects.filter(email=email).exists() or User.objects.filter(phone_number=phone_number).exists():
            return JsonResponse({'message':'User has already been registered','status':'fail'})
        else:
            user = User.objects.create(
                first_name=first_name, last_name=last_name, phone_number=phone_number, email=email,username = username, registered_as = registered_as, faculty=faculty, department=department
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
            
    return render(request, 'login.html', {'users':users})

def export_excel(request):
    fields = ['email', 'first_name', 'last_name', 'phone_number', 'registered_as', 'faculty', 'department']

    # Query the data from the User model
    users = User.objects.values(*fields)

    # Create a DataFrame from the query result
    df = pd.DataFrame(users)

    # Write the DataFrame to an in-memory buffer as Excel file
    excel_buffer = BytesIO()
    df.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)  # Set the buffer's file pointer to the beginning

    # Create an HTTP response with the Excel file as content
    response = HttpResponse(excel_buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Set the Content-Disposition header to trigger a download
    response['Content-Disposition'] = 'attachment; filename="registration.xlsx"'

    return response