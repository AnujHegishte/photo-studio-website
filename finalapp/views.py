from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail

from .forms import FbForm
from .models import FbModel
from random import randrange
import folium

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("ulogin")


def ulogin(request):
    if request.user.is_authenticated:
        return redirect("home")
    elif request.method =="POST":
        un=request.POST.get("un")
        pw=request.POST.get("pw")
        ur=authenticate(username=un, password=pw)
        if ur is not None:
            login(request, ur)
            return redirect("home")
        else:
            return render(request, "login.html",{"login_msg": "Invalid login"})
    else:
        return render(request, "login.html")


def usignup(request):
    if request.method == "POST":
        un=request.POST.get("un")
        pw1=request.POST.get("pw1")
        pw2=request.POST.get("pw2")
        if pw1==pw2:
            try:
                ur=User.objects.get(username=un)
                return render(request,"signup.html", {"su_msg":"User already exists"})
            except User.DoesNotExist:
                ur=User.objects.create_user(username=un, password=pw1)
                ur.save()
                return redirect("ulogin")
        else:
            return render(request, "signup.html", {"su_msg":"Passwords did not match"})
    else:
        return render(request, "signup.html")


def settings(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            un=request.POST.get("un")
            pw1=request.POST.get("pw1")
            pw2=request.POST.get("pw2")
            if pw1==pw2:
                try:
                    ur=User.objects.get(username=un)
                    ur.set_password(pw1)
                    ur.save()
                    return redirect("home")
                except User.DoesNotExist:
                    return render(request, "settings.html", {"st_msg":"User does not exist"})
            else:
                return render(request, "settings.html", {"st_msg":"Passwords did not match"})
        else:
            return render(request, "settings.html")
    else:
        return redirect ("ulogin")


def ulogout(request):
    logout(request)
    return redirect("ulogin")


def uforgotpassword(request):
    if request.method == "POST":
        un=request.POST.get("un")
        try:
            ur=User.objects.get(username=un)
            text="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            pw=""
            for i in range(8):
                pw=pw+text[randrange(len(text))]
                ur.set_password(pw)
                ur.save()
            send_mail("New Password","Your new password is " +str(pw), "krystaldigital20@gmail.com", [str(un)])
            return redirect("ulogin")
        except User.DoesNotExist:
            return render(request, "forgotpassword.html", {"fp_msg":"User does not exist"})            
    else:
        return render(request, "forgotpassword.html")
   

def contact(request):
    lat_lng=[19.392560, 72.825810]
    f=folium.Figure(width=500, height=500)
    vasai=folium.Map(location=lat_lng, zoom_start=16).add_to(f)
    folium.Marker(lat_lng, tooltip="Krystal Image Photo Studio", tooltip_color="red").add_to(vasai)
    vasai_html=vasai._repr_html_()
    return render(request, 'contact.html',{"msg":vasai_html})


def feedback(request):
    if request.method =="POST":
        data = FbForm(request.POST) 
        if data.is_valid():
            data.save()
            msg="Thank you for your feedback."
            fm=FbForm()
            return render(request,'feedback.html',{'fm':fm,'fb_msg':msg})
        else:
            fm=FbForm()
            return render(request,'feedback.html',{'fm':fm,'fb_msg':data})
    else:
        fm=FbForm()
        return render(request,'feedback.html',{'fm':fm})


def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')