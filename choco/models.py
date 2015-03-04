from django.db import models
from django.contrib.auth.models import User
from django import forms


class Chocobo(models.Model):
    name = models.CharField(max_length=100)
    speed_stars = models.IntegerField()
    acc_stars = models.IntegerField()
    end_stars = models.IntegerField()
    stamina_stars = models.IntegerField()
    cunning_stars = models.IntegerField()
    speed_stat = models.IntegerField(blank=True)
    acc_stat = models.IntegerField( blank=True)
    end_stat = models.IntegerField( blank=True)
    stamina_stat = models.IntegerField( blank=True)
    cunning_stat = models.IntegerField( blank=True)
    sex = models.CharField(max_length=1)
    color = models.ForeignKey("Color", blank=True); 
    ability_h = models.ForeignKey("Ability", related_name="+", blank=True)
    ability_a = models.ForeignKey("Ability",  related_name="+", blank=True)
    rank = models.IntegerField( blank=True)
    rating = models.IntegerField( blank=True)
    weather = models.ForeignKey("Weather", blank=True)
    img_link = models.CharField(max_length=200, blank=True)
    speed_source = models.CharField(max_length=1, blank=True)
    acc_source = models.CharField(max_length=1,  blank=True)
    end_source = models.CharField(max_length=1, blank=True)
    stamina_source = models.CharField(max_length=1, blank=True)
    cunning_source = models.CharField(max_length=1, blank=True)
    mother = models.ForeignKey("Chocobo",related_name="+", blank=True, null=True)
    father = models.ForeignKey("Chocobo",related_name="+", blank=True, null=True)
    def __unicode__(self):
        return "{} ".format(self.name)

class Weather(models.Model):
    name = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to = "uploads")
    img2 = models.ImageField(upload_to = "uploads")
    img3 = models.ImageField(upload_to = "uploads")
    def __unicode__(self):
        return "{} ".format(self.name)
        
class Color(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to = "uploads")
    def __unicode__(self):
        return "{} ".format(self.name)

class Ability(models.Model):
    name = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to = "uploads")
    def __unicode__(self):
        return "{} ".format(self.name)
        