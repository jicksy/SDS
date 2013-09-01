# Create your views here.
from reports.models import *
from user_profiles.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def view_institution(request):
    send_dict = {}
    inst = Institution.objects.all()
    send_dict['inst'] = inst
    return render_to_response('admin/view_insti.html',send_dict,context_instance=RequestContext(request))

def view_item(request):
	send_dict ={}
	item = Item.objects.all()
	send_dict['item'] = item
	return render_to_response('admin/view_item.html',send_dict, context_instance=RequestContext(request))

def view_location(request):
    send_dict = {}
    region=Region.objects.all()
    subregion=SubRegion.objects.all()
    send_dict['region']=region
    send_dict['subregion']=subregion
    return render_to_response('admin/view_location.html',send_dict,context_instance=RequestContext(request))

def view_salesperson(request):
    send_dict ={}
    salesperson =SalesPerson.objects.all()
    send_dict['salesperson']=salesperson
    report=Report.objects.all()
    send_dict['report']=report
    return render_to_response('admin/view_salesperson.html', send_dict,context_instance=RequestContext(request))
