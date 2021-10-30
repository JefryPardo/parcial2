from django.db import models

class Calificacion(models.Model):
    idcalificacion = models.AutoField(db_column='IdCalificacion', primary_key=True)  # Field name made lowercase.
    descripcioncalificacion = models.CharField(db_column='DescripcionCalificacion', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'calificacion'
