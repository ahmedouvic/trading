from django.conf.urls import patterns, include, url



urlpatterns = patterns('apps.extra.views',
    url(r'^contact-us/$', 'contact_us', name='contact_us'),
)
