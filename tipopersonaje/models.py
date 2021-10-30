from django.db import models

class Tipopersonaje(models.Model):
    idtipopersonaje = models.IntegerField(db_column='IdTipoPersonaje', primary_key=True)  # Field name made lowercase.
    nombretipopersonaje = models.CharField(db_column='NombreTipoPersonaje', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipopersonaje'
