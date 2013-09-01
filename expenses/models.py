from django.db import models
from reports.models import Institution
from user_profiles.models import SalesPerson
# Create your models here.

class Expense(models.Model):
    salesperson = models.ForeignKey(SalesPerson)
    institution = models.ForeignKey(Institution)
    date = models.DateField()

    def __unicode__(self):
        return (self.salesperson.name+" "+(self.institution.name)+" "+(self.date.strftime('%m/%d/%Y')))

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
    
class ExpenseDetail(models.Model):
    expense = models.ForeignKey(Expense)
    institution = models.ForeignKey(Institution)
    details = models.CharField(max_length = 30)
    amount = models.IntegerField()
    #bill=models.ImageField(upload_to = "/uploads/bills",storage=,height_field= 150,width_field= 150,max_length=)
    timeStamp = models.DateTimeField()

    def __unicode__(self):
        return self.details

    class Meta:
        verbose_name = "Expense detail"
        verbose_name_plural = "Expense details"

    def save(self, *args, **kwargs ):
        self.expense=expense
        self.institution=expense.institution
        super(Expense, self).save(*args, **kwargs)
