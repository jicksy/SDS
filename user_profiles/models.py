from django.db import models
from django.contrib.auth.models import User
from reports.models import Institution
# Create your models here.

class SalesPerson(models.Model):
    user = models.OneToOneField(User)
    #institution = models.ForeignKey(Institution)
    contactNumber = models.PositiveIntegerField(max_length = 10)

    class Meta:
        verbose_name = "Sales person"
        verbose_name_plural = "Sales persons"

    def __unicode__(self):
        return self.user.username