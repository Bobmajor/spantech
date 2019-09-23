from django.urls import path, include

from span.views import index, about, services, team, fqa

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('team/', team, name='team'),
    path('fqa/', fqa, name='fqa'),
]