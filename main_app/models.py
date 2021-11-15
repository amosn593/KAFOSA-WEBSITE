from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(max_length=255)
    register_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-register_date',)

    def __str__(self):
        return self.name


class TurtleBay(models.Model):
    name = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    register_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-register_date',)

    def __str__(self):
        return self.name
