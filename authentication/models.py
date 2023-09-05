from django.db import models
from django.utils.translation import gettext as _

class Register(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=30)
    Confirm_Password = models.CharField(max_length=30)

class Movie3(models.Model):
    Movie_Name = models.CharField(_("Movie_Name"),max_length=500)
    Theatre_Name = models.CharField(_("Theatre_Name"),max_length=200)
    Theatre_Location = models.CharField(_("Theatre_Location"),max_length=200)
    Release_Date = models.DateField(_("Release_Date"),auto_now=True, help_text="Format: YYYY-MM-DD")
    URL = models.CharField(_("URL"),max_length=500)
