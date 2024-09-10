from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is Invalid!!!")

    return render(request, 'login.html')


def signuppage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_data = User.objects.create_user(username,email,password)
        user_data.save()
        return redirect("login")

    return render(request, "signup.html")

def homepage(request):
    return render(request, 'home.html')