"""Vistas para el modelo de Personas"""
from rest_framework import generics

from personas.models import Persona, TipoDocumento
from personas.serializers import PersonaSerializer, TipoDocumentoSerializer


class PersonaList(generics.ListCreateAPIView):
    """Clase para Persona"""
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonaDetail(generics.RetrieveUpdateDestroyAPIView):
    """Clase para Persona"""
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class TipoDocumentoList(generics.ListCreateAPIView):
    """Clase para TipoDocumento"""
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer


class TipoDocumentoDetail(generics.RetrieveUpdateDestroyAPIView):
    """Clase para TipoDocumento"""
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
