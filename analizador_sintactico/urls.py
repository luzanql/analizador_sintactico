from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('polls.views',

                       # Examples:
                       # url(r'^$', 'PLN.views.home', name='home'),

                       url(r'^$', 'index', name='index'),

                       
)
