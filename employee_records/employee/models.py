from django.db import models

# Create your models here.
class feedbackus(models.Model):
    fname = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    message = models.CharField(max_length=200,null=True)

class employee(models.Model):
    empid = models.CharField(max_length=30,null=True)
    fname = models.CharField(max_length=30,null=True)
    lname = models.CharField(max_length=30,null=True)
    dep = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=30,null=True)
    country = models.CharField(max_length=30,null=True)
    state = models.CharField(max_length=30,null=True)
    city = models.CharField(max_length=30,null=True)
    dob = models.CharField(max_length=30,null=True)
    doj = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    con_password = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)