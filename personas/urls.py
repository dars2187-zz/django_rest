"""Urls para el modelo de Personas"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from personas import views

urlpatterns = [
    url(r'^personas/$', views.PersonaList.as_view()),
    url(r'^personas/(?P<pk>\d+)/$', views.PersonaDetail.as_view()),
    url(r'^tiposDocumento/$', views.TipoDocumentoList.as_view()),
    url(r'^tiposDocumento/(?P<pk>\d+)/$', views.TipoDocumentoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
