from django import forms
from reports.models import *
from user_profiles.models import *
from django.forms.extras.widgets import SelectDateWidget

def get_salesperson_choices():
    return ([(c.id, c.user.username) for c in SalesPerson.objects.all()])

def get_region_choices():
    return ([(c.id, c.name) for c in Region.objects.all()])

def get_sub_region_choices():
    return ([(c.id, c.name) for c in SubRegion.objects.all()])

def get_institution_choices():
    return ([(c.id, c.name) for c in Institution.objects.all()])

def get_item_category_choices():
    return ([(c.id, c.name) for c in ItemCategory.objects.all()])

def get_item_choices():
    return ([(c.id, c.name) for c in Item.objects.all()])

class RegionForm (forms.ModelForm):
    
    class Meta:
        model = Region

class SubRegionForm (forms.ModelForm):
    
    class Meta:
        model = SubRegion

    def __init__(self, *args, **kwargs):
        super(SubRegionForm, self).__init__(*args, **kwargs)

class InstitutionForm (forms.ModelForm):
    
    class Meta:
        model = Institution

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)

class InstitutionStaffForm (forms.ModelForm):

    class Meta:
        model = InstitutionStaff

    def __init__(self, *args, **kwargs):
        super(InstitutionStaffForm, self).__init__(*args, **kwargs)

class ItemCategoryForm (forms.ModelForm):

    class Meta:
        model = ItemCategory

class ItemForm (forms.ModelForm):
    
    class Meta:
        model = Item

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)

class ReportForm (forms.ModelForm):
    date = forms.DateField(required = True, widget = SelectDateWidget)
    meeting_note = forms.CharField(required = True, widget=forms.Textarea, max_length = 50)

    class Meta:
        model = Report
        exclude = ['salesperson','report','timeStamp']

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)


class AddSaleForm (forms.ModelForm):

    class Meta: 
        model=InstitutionPurchase
        exclude = ['report','institution','timeStamp',]


class AddScopeForm (forms.ModelForm):

    class Meta: 
        model=InstitutionFurtherPurchase
        exclude = ['report','institution',]


class VisitForm (forms.ModelForm):
    
    class Meta:
        model = Visit
        exclude = ['salesperson',]

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
