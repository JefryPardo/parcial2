from django.db import models

class Rol(models.Model):
    idrol = models.IntegerField(db_column='IdRol', primary_key=True)  # Field name made lowercase.
    nombrerol = models.CharField(db_column='NombreRol', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rol'