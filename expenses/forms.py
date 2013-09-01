from django.forms import ModelForm
from expenses.models import *
from reports.models import *
from user_profiles.models import *
from reports.forms import *

class ExpenseForm(ModelForm):
    
    class Meta:
        model = Expense
        exclude = ['salesperson',]

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)

class AddExpenseForm (forms.ModelForm):

    class Meta: 
        model=ExpenseDetail
        exclude = ['institution','expense','timeStamp',]
        