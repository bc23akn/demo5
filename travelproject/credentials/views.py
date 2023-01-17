
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    if request.method== 'POST':
        username1 = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username1,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username1 = request.POST['username']
        firstname1 = request.POST['firstname']
        lastname1 = request.POST['lastname']
        email1= request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username1).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email1).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username1,first_name=firstname1,last_name=lastname1,email=email1,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render( request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')