from django.db import models
from pelicula.models import Pelicula
from personas.models import Persona
from tipopersonaje.models import Tipopersonaje
from rol.models import Rol


class Reparto(models.Model):
    idreparto = models.AutoField(db_column='IdReparto', primary_key=True)  # Field name made lowercase.
    idpelicula = models.ForeignKey(Pelicula, models.DO_NOTHING, db_column='IdPelicula')  # Field name made lowercase.
    idactor = models.ForeignKey(Persona, models.DO_NOTHING, db_column='IdActor')  # Field name made lowercase.
    idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='IdRol')  # Field name made lowercase.
    idtipopersonaje = models.ForeignKey(Tipopersonaje, models.DO_NOTHING, db_column='IdTipoPersonaje')  # Field name made lowercase.
    personajes = models.TextField(db_column='Personajes')  # Field name made lowercase.
    premio = models.TextField(db_column='Premio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reparto'
        unique_together = (('idpelicula', 'idactor'),)
