from django.db import models
from django.contrib.auth.models import User
from django import forms


class Chocobo(models.Model):
    name = models.CharField(max_length=100)
    pedigree = models.CharField(max_length=2,blank=True, null=True)
    speed_stars = models.IntegerField()
    acc_stars = models.IntegerField()
    end_stars = models.IntegerField()
    stamina_stars = models.IntegerField()
    cunning_stars = models.IntegerField()
    speed_stat = models.IntegerField(blank=True, null=True)
    acc_stat = models.IntegerField( blank=True, null=True)
    end_stat = models.IntegerField( blank=True, null=True)
    stamina_stat = models.IntegerField( blank=True, null=True)
    cunning_stat = models.IntegerField( blank=True, null=True)
    sex = models.CharField(max_length=1)
    color = models.ForeignKey("Color", blank=True); 
    ability_h = models.ForeignKey("Ability", related_name="+", blank=True, null=True)
    ability_a = models.ForeignKey("Ability",  related_name="+", blank=True, null=True)
    rank = models.IntegerField( blank=True, null=True)
    rating = models.IntegerField( blank=True, null=True)
    weather = models.ForeignKey("Weather", blank=True, null=True)
    img_link = models.CharField(max_length=200, blank=True, null=True)
    speed_source = models.CharField(max_length=1, blank=True, null=True)
    acc_source = models.CharField(max_length=1,  blank=True, null=True)
    end_source = models.CharField(max_length=1, blank=True, null=True)
    stamina_source = models.CharField(max_length=1, blank=True, null=True)
    cunning_source = models.CharField(max_length=1, blank=True, null=True)
    mother = models.ForeignKey("Chocobo",related_name="+", blank=True, null=True)
    father = models.ForeignKey("Chocobo",related_name="+", blank=True, null=True)
    jockey = models.ForeignKey(User)
    def __unicode__(self):
        return "{} ".format(self.name)

class Weather(models.Model):
    name = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to = "choco\static")
    img2 = models.ImageField(upload_to = "choco\static")
    img3 = models.ImageField(upload_to = "choco\static")
    def __unicode__(self):
        return "{} ".format(self.name)
        
class Color(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "choco\static")
    def __unicode__(self):
        return "{} ".format(self.name)

class Ability(models.Model):
    name = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to = "choco\static")
    def __unicode__(self):
        return "{} ".format(self.name)
  
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    