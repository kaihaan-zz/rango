'''
Created on Jul 12, 2017

@author: jwang02
'''
from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
]
