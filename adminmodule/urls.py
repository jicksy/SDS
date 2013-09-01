from django.conf.urls import patterns, include, url
from adminmodule import views


urlpatterns =patterns('',
     url(r'^view_institution$', views.view_institution, name="institution-view"),        
     url(r'^view_item$', views.view_item, name='item-view'),
     url(r'^view_location$', views.view_location, name="location-view"),
     url(r'^view_salesperson$', views.view_salesperson, name="salesperson-view"),
)