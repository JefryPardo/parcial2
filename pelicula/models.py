from django.db import models

from calificacion.models import Calificacion
from personas.models import Persona
from genero.models import Genero
from tipocalidad.models import Tipocalidad
from productora.models import Productora

class Pelicula(models.Model):
    idpelicula = models.AutoField(db_column='IdPelicula', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=150)  # Field name made lowercase.
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='IdGenero')  # Field name made lowercase.
    idcalificacion = models.ForeignKey(Calificacion, models.DO_NOTHING, db_column='IdCalificacion')  # Field name made lowercase.
    imagen = models.CharField(db_column='Imagen', max_length=250, blank=True, null=True)  # Field name made lowercase.
    trailer = models.CharField(db_column='Trailer', max_length=250, blank=True, null=True)  # Field name made lowercase.
    duracionhoras = models.IntegerField(db_column='DuracionHoras')  # Field name made lowercase.
    duracionminutos = models.IntegerField(db_column='DuracionMinutos')  # Field name made lowercase.
    idtipocalidad = models.ForeignKey(Tipocalidad, models.DO_NOTHING, db_column='IdTipoCalidad')  # Field name made lowercase.
    iddirector = models.ForeignKey(Persona, models.DO_NOTHING, db_column='IdDirector')  # Field name made lowercase.
    premiosrecibidos = models.TextField(db_column='PremiosRecibidos', blank=True, null=True)  # Field name made lowercase.
    idproductora = models.ForeignKey(Productora, models.DO_NOTHING, db_column='IdProductora')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pelicula'