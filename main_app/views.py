from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils.html import strip_tags
from kafosa.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TurtleBay


def index(request):
    return render(request, "main_app/home.html")


# membership
def membership(request):
    return render(request, "main_app/members/qualification.html")


def application(request):
    return render(request, "main_app/members/application.html")


def memmberlist(request):
    return render(request, "main_app/members/members.html")


def gallery(request):
    return render(request, "main_app/gallery/gallery.html")


def contact_us(request):
    return render(request, "main_app/contact/contact.html")


def objectives(request):
    return render(request, "main_app/about/objectives.html")


def kafosa(request):
    return render(request, "main_app/news/cafosa.html")


def turtlebay(request):
    return render(request, "main_app/news/turtlebay.html")

def finsco(request):
    return render(request, "main_app/news/kafosa_finsco.html")
