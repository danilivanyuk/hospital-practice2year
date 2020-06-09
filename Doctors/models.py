from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True) #Doctor's name
    email = models.CharField(max_length=200, null=True) #Doctor's email

    def __str__(self):
        return self.name

class Client(models.Model):
    CATEGORY = (
        ('УЗИ','УЗИ'),
        ('ЭХОКАРДИОГРАФИЯ','ЭХОКАРДИОГРАФИЯ'),
    )
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250, null=True) #Client's name
    phone = models.CharField(max_length=12, null=True)
    cost = models.FloatField() # Price
    category = models.CharField(max_length=200, null=True, choices=CATEGORY) #Choose category from CATEGORY
    additionalInfo = models.CharField(max_length=250, null=True)
    analys_pic = models.ImageField(null=True, blank=True)
    current_visit = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    next_visit = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
    