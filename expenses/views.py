# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from expenses.models import *
from reports.models import *
from user_profiles.models import *
from expenses.forms import *


def add_expense(request):
    dict = {}
    AddExpenseDetailFormSet = inlineformset_factory(Expense,
        ExpenseDetail,
        exclude=['expense','institution','timeStamp'],
        extra=1)
    new_detail = AddExpenseDetailFormSet(prefix='detail')
    form = ExpenseForm()
    print request.POST
    if request.POST:
        form = ExpenseForm(request.POST)
        if 'add_more' in request.POST:
            cp = request.POST.copy()
            new_detail = AddExpenseForm(request.POST)
            cp['detail-TOTAL_FORMS'] = int(cp['detail-TOTAL_FORMS'])+ 1
            new_detail = AddExpenseDetailFormSet(cp,prefix='detail')
        elif form.is_valid():
            print "Form Valid"
            data = form.cleaned_data
            salesperson = request.user
            institution = Institution.objects.get(name__iexact = data['institution'])
            q = Expense.objects.filter(
                salesperson = salesperson, 
                institution = institution,
                date = data['date'])
            if q.count() > 0:
                messages.add_message(request, messages.INFO, 
                    "The Expense Already Exists.")
            else:
                expense = Expense()
                expense.salesperson = salesperson
                expense.institution = institution
                expense.date = data['date']
                expense.save()
                detail_formset = AddExpenseDetailFormSet(request.POST, 
                    request.FILES, prefix='detail')
                if detail_formset.is_valid():
                    detail_formset.save(Expense)
                form = ExpenseForm()
                messages.add_message(request, messages.INFO,
                    "You have successfully added a new expense.")
    dict['form'] = form
    dict['detail'] = new_detail
    return render_to_response(
        'expenses/add_expense.html',dict,
        context_instance=RequestContext(request))