from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import trains.urls
from route.views import *
from station.views import *
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^trains/', include(trains.urls, namespace='trains')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^route/(?P<train_id>\d+)$', get_route_by_train, name='route'),
    url(r'^search/', get_form, name='search'),
    url(r'^display/', find_trains, name='display'),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('',
                        url(r'^captcha/', include('captcha.urls')),
                        )

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
