from django.conf.urls import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('polls.views',

                       # Examples:
                       # url(r'^$', 'PLN.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'index', name='index'),

                       )