from django.db import models

class Tipocalidad(models.Model):
    idtipocalidad = models.AutoField(db_column='IdTipoCalidad', primary_key=True)  # Field name made lowercase.
    nombretipocalidad = models.CharField(db_column='NombreTipoCalidad', unique=True, max_length=45)  # Field name made lowercase.
    descripcioncalidad = models.CharField(db_column='DescripcionCalidad', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipocalidad'