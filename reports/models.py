from django.db import models
from django.contrib.auth.models import User
from user_profiles.models import *
#from expenses.models import *

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length = 30, unique = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

class SubRegion(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length = 30, unique = True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Subregion"
        verbose_name_plural = "Subregions"

class Institution(models.Model):
    name = models.CharField(max_length = 40, unique = True)
    region = models.ForeignKey(Region)
    subregion = models.ForeignKey(SubRegion)
    pin_code = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"

class InstitutionStaff(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    #image = models.ImageField(upload_to = "/uploads/staff",storage=,height_field= 150,width_field= 150,max_length=)
    designation = models.CharField(max_length = 30)
    institution = models.ForeignKey(Institution)

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name = "Institution staff"
        verbose_name_plural = "Institution staffs"

class ItemCategory(models.Model):
    name = models.CharField(max_length = 30, unique = True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Item(models.Model):
    grade = models.CharField(max_length = 10)
    subject = models.ForeignKey(ItemCategory)
    name = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

class Report(models.Model):
    salesperson = models.ForeignKey(User)
    institution = models.ForeignKey(Institution)
    date = models.DateField()
    meeting_note = models.TextField(max_length = 50) 
    stage_of_negotiation = models.CharField(max_length = 30)
    timeStamp = models.DateTimeField()

    def __unicode__(self):
        return (self.institution.name+" "+(self.date.strftime('%m/%d/%Y')))

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

class InstitutionPurchase(models.Model):
    report = models.ForeignKey(Report)
    institution = models.ForeignKey(Institution)
    sale_item = models.ForeignKey(Item)
    sale_count = models.IntegerField()
    timeStamp = models.DateTimeField()

    def __unicode__(self):
        return self.institution.name

    class Meta:
        verbose_name = "Institution purchase"
        verbose_name_plural = "Institution purchases"

class InstitutionFurtherPurchase(models.Model):
    report = models.ForeignKey(Report)
    institution = models.ForeignKey(Institution)
    scope_item = models.ForeignKey(Item)
    scope_count = models.IntegerField()

    def __unicode__(self):
        return self.institution.name

    class Meta:
        verbose_name = "Institution further purchase"
        verbose_name_plural = "Institution further purchases" 

class Visit(models.Model):
    institution = models.ForeignKey(Institution)
    date = models.DateField()
    salesperson = models.ForeignKey(User)

    def __unicode__(self):
        return self.institution.name

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"