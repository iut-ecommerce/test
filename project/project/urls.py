from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main_app.views.index'),
    url(r'^index$', 'main_app.views.index'),
    url(r'^services', 'main_app.views.services'),
    )