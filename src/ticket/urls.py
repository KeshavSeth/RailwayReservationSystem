from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns(
    '',
    url(r'^bookTicket/(?P<train_id>\d+)/(?P<coach_id>\d+)/',
        views.get_availability, name='booking'),
    url(r'^bookPassenger/', views.passenger_form,name="passenger")

)

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
