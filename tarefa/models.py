from django.db import models

from django.db import models

from core.models import Area, Tipo, TipoTarefa

# Vamos aprender juntos kk!
from trabalho.models import Trabalho


class Tarefa(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_tarefa")
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)
    data_realizacao = models.DateField(blank=True, null=True, db_column="data_realizacao")
    tipo_tarefa = models.ForeignKey(TipoTarefa, models.DO_NOTHING, db_column='id_tipo', blank=True, null=True)
    trabalho = models.ForeignKey(Trabalho, models.DO_NOTHING, db_column='id_trabalho', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = "tarefa"
        managed = True
