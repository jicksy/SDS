from django.conf.urls import patterns, include, url
from user_profiles import views

urlpatterns =patterns('',
    url(r'^$', views.login_view, name='login'),
    url(r'^adminhome/$',views.admin_view, name='admin_home'),
    url(r'^home/$', views.user_view, name='user_home'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout'),
)