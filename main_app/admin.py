from django.contrib import admin
from .models import TurtleBay, ContactUs

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message', 'register_date')
    search_fields = ['name', 'phone', 'email']


admin.site.register(ContactUs, ContactAdmin)


class TurtleBayAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'phone', 'email', 'register_date')
    search_fields = ['name', 'phone', 'email', 'organization']


admin.site.register(TurtleBay, TurtleBayAdmin)
