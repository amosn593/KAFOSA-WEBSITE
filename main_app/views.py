from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
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


def contact_form(request):
    if request.method == 'POST':
        name = request.POST["name"].strip()
        organization = request.POST["organization"].strip()
        phone = request.POST["phone"].strip()
        email = request.POST["email"].strip()
        try:
            register = TurtleBay(
                name=name, organization=organization, phone=phone, email=email)
            register.save()
            try:
                context = {
                    "name": name,
                    "organization": organization,
                    "phone": phone,
                    "email": email,
                }
                subject = 'KAFOSA WORKSHOP REGISTRATION'
                html_message = render_to_string(
                    'main_app/emails/turtle.html', context)
                plain_message = strip_tags(html_message)
                from_email = 'workshop@kafosa.or.ke'
                to = email
                to1 = 'info@kafosa.or.ke'
                to2 = 'workshop@kafosa.or.ke'
                send_mail(subject, plain_message, from_email,
                          [to, to1, to2], html_message=html_message)
                messages.success(
                    request, f"Workshop Registration sent successfully.")

                return redirect('turtlebay')
            except:
                messages.error(
                    request, f"Something went wrong, kindly try again!!!")
                return redirect('turtlebay')
        except:
            messages.error(
                request, f"Something went wrong, kindly try again!!!")
            return redirect('turtlebay')

    else:
        return redirect('home')
