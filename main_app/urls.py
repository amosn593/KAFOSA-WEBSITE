from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('kafosa-membership_qualification', membership, name="qualification"),
    path('kafosa-membership_application', application, name="application"),
    path('kafosa-membership_list', memmberlist, name="memmberlist"),
    path('kafosa-gallery', gallery, name="gallery"),
    path('kafosa-contacts', contact_us, name="contact_us"),
    path('kafosa-objectives', objectives, name="objectives"),
    path('cafosa_launch', kafosa_lauch, name="kafosa"),
    path('kafosa-workshop-5-7-2022', workshop_2022, name="workshop_2022"),
    path('kafosa-workshop-15-18-2021', workshop_2021, name="workshop_2021"),
    path('kafosa-partners-with-finsco-africa', finsco, name="finsco"),
]
