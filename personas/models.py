from django.db import models

class Persona(models.Model):
    idpersona = models.IntegerField(db_column='IdPersona', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=45)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=45)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento')  # Field name made lowercase.
    ciudadnacimiento = models.CharField(db_column='CiudadNacimiento', max_length=45)  # Field name made lowercase.
    paisnacimiento = models.CharField(db_column='PaisNacimiento', max_length=45)  # Field name made lowercase.
    esdirector = models.IntegerField(db_column='EsDirector')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'