from django.conf.urls import patterns, include, url
from django.contrib.auth import views


urlpatterns= patterns('',
    url(r'^reset/$', views.password_reset, {'template_name': 'password_reset/password_reset_form.html',
        'email_template_name':'password_reset/password_reset_email.html',
        'post_reset_redirect':'done',
        'subject_template_name':'password_reset/password_reset_subject.txt',}, name="password_reset"),
    url(r'^reset/done/$', views.password_reset_done,
        {'template_name': 'password_reset/password_reset_done.html',}, 
        name="password_reset_done"),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm,
        {'template_name': 'password_reset/password_reset_confirm.html',
        'post_reset_redirect':'/password/done'},
        name="password_reset_confirm"),
    url(r'^done/$',views.password_reset_complete,
        {'template_name': 'password_reset/password_reset_complete.html',},
        name="password_reset_complete"),)