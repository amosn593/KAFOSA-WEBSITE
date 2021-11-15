from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.html import strip_tags
from kafosa.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TurtleBay, ContactUs


def index(request):
    if request.method == "GET":
        return render(request, "main_app/home.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


# membership
def membership(request):
    if request.method == "GET":
        return render(request, "main_app/members/qualification.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


def application(request):
    if request.method == "GET":
        return render(request, "main_app/members/application.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


def memmberlist(request):
    if request.method == "GET":
        return render(request, "main_app/members/members.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


def gallery(request):
    if request.method == "GET":
        return render(request, "main_app/gallery/gallery.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


def contact_us(request):
    if request.method == "GET":
        return render(request, "main_app/contact/contact.html")
    elif request.method == "POST":
        name = request.POST["name"].strip()
        phone = request.POST["phone"]
        email = request.POST["email"].strip()
        message = request.POST["message"].strip()
        try:
            c = ContactUs(name=name, phone=phone, email=email, message=message)
            c.save()
            return redirect('contact_us')
        except:
            return redirect('home')
    else:
        return HttpResponse("INVALID HTTP METHOD")


def objectives(request):
    if request.method == "GET":
        return render(request, "main_app/about/objectives.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


def kafosa(request):
    if request.method == "GET":
        return render(request, "main_app/news/cafosa.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


def turtlebay(request):
    if request.method == "GET":
        return render(request, "main_app/news/turtlebay.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


def finsco(request):
    if request.method == "GET":
        return render(request, "main_app/news/kafosa_finsco.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")
