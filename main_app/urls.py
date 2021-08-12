from django.urls import path
from .views import index, membership, application, memmberlist, contact_us, objectives, kafosa, turtlebay, contact_form

urlpatterns = [
    path('', index, name="home"),
    path('kafosa-membership_qualification', membership, name="qualification"),
    path('kafosa-membership_application', application, name="application"),
    path('kafosa-membership_list', memmberlist, name="memmberlist"),
    path('kafosa-contacts', contact_us, name="contact_us"),
    path('kafosa-objectives', objectives, name="objectives"),
    path('cafosa_launch', kafosa, name="kafosa"),
    path('kafosa-workshop-15-18-21', turtlebay, name="turtlebay"),
    path('workshop_register', contact_form, name="register"),
]
