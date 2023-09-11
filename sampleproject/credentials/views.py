from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User")
            return redirect('login')
    return render(request,"login.html")
def reg(request):
    if request.method == 'POST':
        username=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cnf_password=request.POST['cnfpassword']
        if password==cnf_password:
            if User.objects.filter(username=username).exists():
                # this is to display on webpage "Already User exists"
                messages.info(request,"Already User exists")
                # goes to register page itself by giving urls.py name
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Already Email exists")
                return redirect('reg')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                messages.info(request, "Successfully Registered")
                # this would print the message on terminal
                print("User Created")
                # goes to home page
                return redirect('login')
        else:
            messages.info(request, "Password does not match")
            print("Password does not match")
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')