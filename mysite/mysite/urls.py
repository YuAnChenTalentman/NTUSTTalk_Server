from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import hello_world,read_post,write_post


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello_world),
    url(r'^read_post/', read_post),
    url(r'^write_post/', write_post),
)
