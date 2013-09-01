from django.conf.urls import patterns, include, url
from expenses import views

urlpatterns = patterns('',
	url(r'^add_expense$', views.add_expense, name='add_expense'),
	)