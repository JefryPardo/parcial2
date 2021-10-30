from django.db import models

from pelicula.models import Pelicula
from personas.models import Persona

class Actoroscar(models.Model):
    idactoroscar = models.AutoField(db_column='IdActorOscar', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='IdPersona')  # Field name made lowercase.
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    descripcionoscar = models.CharField(db_column='DescripcionOscar', max_length=45)  # Field name made lowercase.
    idpelicula = models.ForeignKey(Pelicula, models.DO_NOTHING, db_column='IdPelicula')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actoroscar'