from django.db import models

# Create your models here.

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ('nombre',)


class Persona(models.Model):
    documento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipoDocumento = models.ForeignKey(
        TipoDocumento,
        on_delete=models.CASCADE,
        related_name="persona_tipo_documento"
    )

    class Meta:
        ordering = ('nombre',)
