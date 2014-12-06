from django.conf.urls import patterns, include, url
from hello import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_project.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^hello/',views.hello,name='hello'),
    url(r'^admin/', include(admin.site.urls)),
)
