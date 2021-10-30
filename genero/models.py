from django.db import models

class Genero(models.Model):
    idgenero = models.AutoField(db_column='IdGenero', primary_key=True)  # Field name made lowercase.
    nombregenero = models.CharField(db_column='NombreGenero', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genero'
