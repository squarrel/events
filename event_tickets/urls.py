from django.urls import path
from django.conf.urls import url
from event_tickets import views


urlpatterns = [
    path('', views.index),
    url(r'^available/(?P<event_id>\d+)$', views.available),
    url(r'^reserve/(?P<event_id>\d+)/(?P<ticket_type>\d+)/(?P<first_name>\w+)/(?P<last_name>\w+)/$', views.reserve),
]
