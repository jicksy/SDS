from django.conf.urls import patterns, include, url
from reports import views

urlpatterns =patterns('',
	url(r'^add_region/$', views.add_region, name='add_region'),
	url(r'^add_subregion/$', views.add_sub_region, name='add_sub_region'),

    url(r'^add_institution/$', views.add_institution, name='add_institution'),
    url(r'^institution/add_staff$', views.add_institution_staff, name='add_institution_staff'),
    url(r'^view_institution$', views.view_institution, name='view_institution'),
    url(r'^institution/add_staff/(?P<inst_id>\d+)/$',views.view_staff,name='view_staff'),
    url(r'^institution/add_visit$', views.add_visit, name='add_visit'),
    url(r'^institution/details/(?P<inst_id>\d+)/$', views.institution_details, name='institution_details'),
    url(r'^institution/view_staff/(?P<inst_id>\d+)/$', views.view_staff,name='view_staff'),

    url(r'^add_item$', views.add_item, name='add_item'),
    url(r'^item/add_category$', views.add_item_category, name='add_item_category'),

    url(r'^add_report$', views.add_report, name='add_report'),
    url(r'^view_report$', views.view_report,name='view_report'),
    url(r'^view_visits$', views.view_visits,name='view_visits'),
    url(r'^report_details/(?P<report_id>\d+)/$',views.report_details, name='report_details'),
)