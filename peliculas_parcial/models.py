# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actoroscar(models.Model):
    idactoroscar = models.AutoField(db_column='IdActorOscar', primary_key=True)  # Field name made lowercase.
    idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='IdPersona')  # Field name made lowercase.
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    descripcionoscar = models.CharField(db_column='DescripcionOscar', max_length=45)  # Field name made lowercase.
    idpelicula = models.ForeignKey('Pelicula', models.DO_NOTHING, db_column='IdPelicula')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actoroscar'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


# class Calificacion(models.Model):
#     idcalificacion = models.AutoField(db_column='IdCalificacion', primary_key=True)  # Field name made lowercase.
#     descripcioncalificacion = models.CharField(db_column='DescripcionCalificacion', unique=True, max_length=45)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'calificacion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


# class Genero(models.Model):
#     idgenero = models.AutoField(db_column='IdGenero', primary_key=True)  # Field name made lowercase.
#     nombregenero = models.CharField(db_column='NombreGenero', unique=True, max_length=45)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'genero'


# class Pelicula(models.Model):
#     idpelicula = models.AutoField(db_column='IdPelicula', primary_key=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre', unique=True, max_length=150)  # Field name made lowercase.
#     anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
#     idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='IdGenero')  # Field name made lowercase.
#     idcalificacion = models.ForeignKey(Calificacion, models.DO_NOTHING, db_column='IdCalificacion')  # Field name made lowercase.
#     imagen = models.CharField(db_column='Imagen', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     trailer = models.CharField(db_column='Trailer', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     duracionhoras = models.IntegerField(db_column='DuracionHoras')  # Field name made lowercase.
#     duracionminutos = models.IntegerField(db_column='DuracionMinutos')  # Field name made lowercase.
#     idtipocalidad = models.ForeignKey('Tipocalidad', models.DO_NOTHING, db_column='IdTipoCalidad')  # Field name made lowercase.
#     iddirector = models.ForeignKey('Persona', models.DO_NOTHING, db_column='IdDirector')  # Field name made lowercase.
#     premiosrecibidos = models.TextField(db_column='PremiosRecibidos', blank=True, null=True)  # Field name made lowercase.
#     idproductora = models.ForeignKey('Productora', models.DO_NOTHING, db_column='IdProductora')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'pelicula'


# class Persona(models.Model):
#     idpersona = models.IntegerField(db_column='IdPersona', primary_key=True)  # Field name made lowercase.
#     nombres = models.CharField(db_column='Nombres', max_length=45)  # Field name made lowercase.
#     apellidos = models.CharField(db_column='Apellidos', max_length=45)  # Field name made lowercase.
#     fechanacimiento = models.DateField(db_column='FechaNacimiento')  # Field name made lowercase.
#     ciudadnacimiento = models.CharField(db_column='CiudadNacimiento', max_length=45)  # Field name made lowercase.
#     paisnacimiento = models.CharField(db_column='PaisNacimiento', max_length=45)  # Field name made lowercase.
#     esdirector = models.IntegerField(db_column='EsDirector')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'persona'


# class Productora(models.Model):
#     idproductora = models.AutoField(db_column='IdProductora', primary_key=True)  # Field name made lowercase.
#     nombreproductora = models.CharField(db_column='NombreProductora', unique=True, max_length=80)  # Field name made lowercase.
#     nombrepais = models.CharField(db_column='NombrePais', max_length=80)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'productora'


# class Reparto(models.Model):
#     idreparto = models.AutoField(db_column='IdReparto', primary_key=True)  # Field name made lowercase.
#     idpelicula = models.ForeignKey(Pelicula, models.DO_NOTHING, db_column='IdPelicula')  # Field name made lowercase.
#     idactor = models.ForeignKey(Persona, models.DO_NOTHING, db_column='IdActor')  # Field name made lowercase.
#     idrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='IdRol')  # Field name made lowercase.
#     idtipopersonaje = models.ForeignKey('Tipopersonaje', models.DO_NOTHING, db_column='IdTipoPersonaje')  # Field name made lowercase.
#     personajes = models.TextField(db_column='Personajes')  # Field name made lowercase.
#     premio = models.TextField(db_column='Premio', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'reparto'
#         unique_together = (('idpelicula', 'idactor'),)


# class Rol(models.Model):
#     idrol = models.IntegerField(db_column='IdRol', primary_key=True)  # Field name made lowercase.
#     nombrerol = models.CharField(db_column='NombreRol', unique=True, max_length=45)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'rol'


# class Tipocalidad(models.Model):
#     idtipocalidad = models.AutoField(db_column='IdTipoCalidad', primary_key=True)  # Field name made lowercase.
#     nombretipocalidad = models.CharField(db_column='NombreTipoCalidad', unique=True, max_length=45)  # Field name made lowercase.
#     descripcioncalidad = models.CharField(db_column='DescripcionCalidad', max_length=45)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tipocalidad'


# class Tipopersonaje(models.Model):
#     idtipopersonaje = models.IntegerField(db_column='IdTipoPersonaje', primary_key=True)  # Field name made lowercase.
#     nombretipopersonaje = models.CharField(db_column='NombreTipoPersonaje', unique=True, max_length=45)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tipopersonaje'
