"""Serializer para el modelo de Personas"""
from rest_framework import serializers
from personas.models import Persona, TipoDocumento


class PersonaSerializer(serializers.ModelSerializer):
    """Clase para Persona"""
    class Meta:
        model = Persona
        fields = ('id', 'documento', 'nombre', 'apellido', 'tipoDocumento')


class TipoDocumentoSerializer(serializers.ModelSerializer):
    """Clase para TipoDocumento"""
    class Meta:
        model = TipoDocumento
        fields = ('id', 'nombre')
