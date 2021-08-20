from django.contrib import admin
from .models import TurtleBay

# Register your models here.


class TurtleBayAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'phone', 'email', 'register_date')


admin.site.register(TurtleBay, TurtleBayAdmin)
