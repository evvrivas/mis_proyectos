from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static  import static 
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}),
    static(settings.MEDIA_ROOT, document_root=settings.MEDIA_URL),
    url(r'^principal/$', pagina_principal), staticfiles_urlpatterns(),


]





if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

