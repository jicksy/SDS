from reports.forms import *
from reports.models import *
from datetime import datetime
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response, redirect
# Create your views here.

def add_region(request):
    dict = {}
    if request.POST:
        form = RegionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            q = Region.objects.filter(name__iexact = data['name'])
            if q.count() > 0:
                messages.add_message(request, messages.INFO, "The region already exists.")
            else:
                region = Region()
                region.name = data['name'].capitalize()
                region.save()
                form = RegionForm()
                messages.add_message(request, messages.INFO, " You have successfully added a new region.")
                #redirect('/')
    else:
        form = RegionForm()
    dict['form'] = form
    return render_to_response('region/add_region.html',dict,context_instance=RequestContext(request))

def add_sub_region(request):
    dict = {}
    if request.POST:
        form = SubRegionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            region = Region.objects.get(name__iexact = data['region'])
            q = SubRegion.objects.filter(name__iexact = data['name'], region = region)
            if q.count() > 0:
                messages.add_message(request, messages.INFO, "The sub region already exists.")
            else:
                region = Region.objects.get(name__iexact = data['region'])
                sub_region = SubRegion()
                sub_region.region = region
                sub_region.name = data['name'].capitalize()
                sub_region.save()
                form = SubRegionForm()
                messages.add_message(request, messages.INFO, " You have successfully added a new sub region to "+region.name)
                #redirect('/')
    else:
        form = SubRegionForm()
    dict['form'] = form
    return render_to_response('region/add_subregion.html',dict,context_instance=RequestContext(request))

def add_institution(request):
    dict = {}
    if request.POST:
        form = InstitutionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            region = Region.objects.get(name__iexact = data['region'])
            subregion = SubRegion.objects.get(name__iexact = data['subregion'])
            q = Institution.objects.filter(name__iexact = data['name'], region = region, subregion = subregion)
            if q.count() > 0:
                messages.add_message(request, messages.INFO, "The institution already exists.")
            else:
                institution = Institution()
                institution.region = region
                institution.subregion = subregion
                institution.name = data['name'].capitalize()
                institution.pin_code = data['pin_code']
                institution.save()
                form = InstitutionForm()
                messages.add_message(request, messages.INFO, " You have successfully added a new institution.")
                #redirect('/')
    else:
        form = InstitutionForm()
    dict['form'] = form
    return render_to_response('institution/add_institution.html',dict,context_instance=RequestContext(request))

def add_institution_staff(request):
    dict = {}
    if request.POST:
        form = InstitutionStaffForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            institution = Institution.objects.get(name = data['institution'])
            q = InstitutionStaff.objects.filter(first_name__iexact = data['first_name'],
                last_name__iexact = data['last_name'], 
                designation__iexact = data['designation'],
                institution = institution)
            if q.count() > 0:
                messages.add_message(request, messages.INFO, "The staff already exists in ."+ institution.name)
            else:
                institution_staff = InstitutionStaff()
                institution_staff.first_name = data['first_name'].capitalize()
                institution_staff.last_name = data['last_name'].capitalize()
                institution_staff.designation = data['designation'].capitalize()
                institution_staff.institution = institution
                institution_staff.save()
                form = InstitutionStaffForm()
                messages.add_message(request, messages.INFO, " You have successfully added a new staff to "+institution.name)
                #redirect('/')
    else:
        form = InstitutionStaffForm()
    dict['form'] = form
    return render_to_response('institution/add_staff.html',dict,context_instance=RequestContext(request))

def add_item_category(request):
    dict = {}
    if request.POST:
        form = ItemCategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            q = ItemCategory.objects.filter(name__iexact = data['name'])
            if q.count() > 0:
                messages.add_message(request, messages.INFO, "The category already exists.")
            else:
                item_category = ItemCategory()
                item_category.name = data['name'].capitalize()
                item_category.save()
                form = ItemCategoryForm()
                messages.add_message(request, messages.INFO, " You have successfully added a new category.")
                #redirect('/')
    else:
        form = ItemCategoryForm()
    dict['form'] = form
    return render_to_response('item/add_item_category.html',dict,context_instance=RequestContext(request))

def add_item(request):
    dict = {}
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            item_category = ItemCategory.objects.get(id = data['subject'])
            q = Item.objects.filter(name__iexact = data['name'], 
                subject = item_category)
            if q.count() > 0:
                messages.add_message(request, messages.INFO, "The item already exists.")
            else:
                item = Item()
                item.name = data['name'].capitalize()
                item.subject = item_category
                item.grade = data['name']
                item.save()
                form = ItemForm()
                messages.add_message(request, messages.INFO, " You have successfully added a new item.")
                #redirect('/')
    else:
        form = ItemForm()
    dict['form'] = form
    return render_to_response('item/add_item.html',dict,context_instance=RequestContext(request))

def add_report(request):
    dict = {}
    AddSaleFormSet = inlineformset_factory(Institution, 
        InstitutionPurchase, 
        exclude=['report','institution','timeStamp'],
        extra=1)
    AddScopeFormSet = inlineformset_factory(Institution, 
        InstitutionFurtherPurchase, 
        exclude=['report','institution'],
        extra=1)
    new_sale = AddSaleFormSet(prefix='sale' )
    new_scope = AddScopeFormSet(prefix='scope')
    form = ReportForm()
    if request.POST:
        form = ReportForm(request.POST)
        if 'add_sale' in request.POST:
            cp = request.POST.copy()
            new_sale = AddSaleForm(request.POST)
            cp['sale-TOTAL_FORMS'] = int(cp['sale-TOTAL_FORMS'])+ 1
            new_sale = AddSaleFormSet(cp,prefix='sale')
            new_scope = AddScopeFormSet(cp,prefix='scope')
        elif 'add_scope' in request.POST:
            cp = request.POST.copy()
            new_scope = AddScopeForm(request.POST)
            cp['scope-TOTAL_FORMS'] = int(cp['scope-TOTAL_FORMS'])+ 1
            new_sale = AddSaleFormSet(cp,prefix='sale')
            new_scope = AddScopeFormSet(cp,prefix='scope')
        elif form.is_valid():
            data = form.cleaned_data
            salesperson = request.user
            institution = Institution.objects.get(name__iexact = data['institution'])
            q = Report.objects.filter(salesperson = salesperson, 
                institution = institution,
                date = data['date'])
            if q.count() > 0:
                messages.add_message(request, messages.INFO, 
                    "The Report Already Exists.")
            else:
                report = Report()
                report.salesperson = salesperson
                report.institution = institution
                report.date = data['date']
                report.meeting_note = data['meeting_note']
                report.stage_of_negotiation = data['stage_of_negotiation'].capitalize()
                report.timeStamp = datetime.now()
                report.save()
                sale_formset = AddSaleFormSet(request.POST, 
                    request.FILES, prefix='sale')
                if sale_formset.is_valid():
                    for form in sale_formset:
                        temp = form.save(commit=False)
                        temp.report=report
                        temp.institution=institution
                        temp.timeStamp = datetime.now()
                        temp.save()
                scope_formset = AddScopeFormSet(request.POST, 
                    request.FILES, prefix='scope')
                if scope_formset.is_valid():
                    for form in scope_formset:
                        temp = form.save(commit=False)
                        temp.report=report
                        temp.institution=institution
                        temp.save()
                form = ReportForm()
                messages.add_message(request, messages.INFO,
                    "You have successfully added a new report.")
    dict['form'] = form
    dict['sale'] = new_sale
    dict['scope'] = new_scope
    return render_to_response(
        'report/add_report.html',dict,
        context_instance=RequestContext(request))

def add_visit(request):
    dict = {}
    if request.POST:
        form = VisitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            institution = Institution.objects.get(name = data['institution'])
            salesperson = request.user
            q = Visit.objects.filter(institution = institution, date = data['date'], salesperson = salesperson)
            if q.count() > 0:
                messages.add_message(request, messages.INFO, "The visit is already added.")
            else:
                visit = Visit()
                visit.institution = institution
                visit.date = data['date']
                visit.salesperson = salesperson
                visit.save()
                form = VisitForm()
                messages.add_message(request, messages.INFO, " You have successfully added a new visit.")
                #redirect('/')
    else:
        form = VisitForm()
    dict['form'] = form
    return render_to_response('institution/add_visit.html',dict,context_instance=RequestContext(request))

def view_institution(request):
    send_dict = {}
    inst = Institution.objects.all()
    send_dict['inst'] = inst
    
    return render_to_response('institution/view_institution.html',send_dict,context_instance=RequestContext(request))

def view_report(request):
    send_dict = {}

    report = Report.objects.filter(salesperson=request.user)
    send_dict['report']=report
    return render_to_response('report/view_report.html',send_dict,context_instance=RequestContext(request))

def view_staff(request,inst_id):
    send_dict = {}
    institute=Institution.objects.get(id=inst_id)
    staff = InstitutionStaff.objects.filter(institution=institute)
    send_dict['staff']=staff
    return render_to_response('institution/view_staff.html',send_dict,context_instance=RequestContext(request))

def institution_details(request,inst_id):
    send_dict = {}
    institute=Institution.objects.get(id=inst_id)
    items=InstitutionPurchase.objects.filter(institution=institute)
    staff=InstitutionStaff.objects.filter(institution=institute)
    send_dict['instt']=institute
    send_dict['items'] = items
    send_dict['staff'] = staff
    sale=InstitutionPurchase.objects.filter(institution=institute)
    scope=InstitutionFurtherPurchase.objects.filter(institution=institute)
    send_dict['report']=report
    send_dict['sale']=sale
    send_dict['scope']=scope
    return render_to_response('institution/details.html',send_dict,context_instance=RequestContext(request))

def view_visits(request):
    send_dict = {}
    visits = Visit.objects.filter(salesperson=request.user)
    send_dict['visits']=visits
    return render_to_response('institution/view_visits.html',send_dict,context_instance=RequestContext(request))

def report_details(request,report_id):
    send_dict = {}
    report=Report.objects.get(id = report_id)
    sale=InstitutionPurchase.objects.filter(report=report)
    scope=InstitutionFurtherPurchase.objects.filter(report=report)
    send_dict['report']=report
    send_dict['sale']=sale
    send_dict['scope']=scope
    return render_to_response('report/report_details.html',send_dict,context_instance=RequestContext(request))



# create views : reports of a salesperson, visits of a salesperson, expenses of a salesperson
# edit view function : add_report, add_visit, in inst. list show inst. related thru report
# save fn()
# melsons work
# show the necessary things in user dashboard avoid others
# create separate dashboard for admin and add necessary things
# 2a vi
# create views for admin