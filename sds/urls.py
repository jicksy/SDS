from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('user_profiles.urls', namespace='Login')),
    url(r'^detail/', include('reports.urls', namespace= 'Detail')),
    url(r'^user/',include('passwordreset.urls', namespace='Passwordreset')),
    url(r'^adminprofile/',include('adminmodule.urls',namespace='Adminprofile')),
    url(r'^salesperson/', include('expenses.urls', namespace='Salesperson')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)