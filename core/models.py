from django.db import models


class Tipo(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_tipo")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = "tipo"
        managed = True


class Area(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_area")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = "area"
        managed = True


class TipoTarefa(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_tipo_tarefa")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = "tipo_tarefa"
        managed = True


class Status(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_status")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = "status_trabalho"
        managed = True
