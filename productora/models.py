from django.db import models

class Productora(models.Model):
    idproductora = models.AutoField(db_column='IdProductora', primary_key=True)  # Field name made lowercase.
    nombreproductora = models.CharField(db_column='NombreProductora', unique=True, max_length=80)  # Field name made lowercase.
    nombrepais = models.CharField(db_column='NombrePais', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productora'
