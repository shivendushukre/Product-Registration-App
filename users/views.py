from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def register(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        password = data['password']
        confirm_password = data['conf_pass']
        regexusername = "^[[A-Z]|[a-z]][[A-Z]|[a-z]|\\d|[_]]{7,29}$"
        regexemail = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.search(regexusername, username):
            return render(request, 'register.html', {'msg': "Username is Not Valid"})
        if not re.search(regexemail, email):
            return render(request, 'register.html', {'msg': "Email ID is not Valid"})
        if password != confirm_password:
            return render(request, 'register.html', {'msg': "Passwords Don't match"})
        if len(password) == 0:
            return render(request, 'register.html', {'msg': "Please enter password"})
        try:
            user = User.objects.create_user(
                username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user.save(using='users_db')
            return render(request, 'product.html', {'msg': 'User Registered Successfully!!'})
        except:
            return render(request, 'register.html', {'msg': 'User already exists'})
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return render(request, 'product.html', {'msg': 'Logged in successfully'})
        return render(request, 'login.html', {'msg': 'Invalid Credentials!!'})
    return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return render(request, 'login.html', {'msg': 'Logged out Successfully'})
    return render(request, 'login.html')
