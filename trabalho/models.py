from django.db import models

from core.models import Area, Tipo, TipoTarefa


# Vamos aprender juntos kk!
class Trabalho(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_trabalho")
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)
    data_inicio = models.DateField(blank=True, null=True, db_column="data_inicio")
    data_entrega = models.DateField(blank=True, null=True, db_column="data_entrega")
    # nome_aluno = models.CharField(max_length=255, blank=True, null=True)
    # email_aluno = models.EmailField('E-mail')
    token = models.CharField(max_length=100)
    id_usuario = models.ForeignKey("accounts.CustomUsuario", on_delete=models.CASCADE, db_column="id_usuario")
    area = models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    tipo = models.ForeignKey(Tipo, models.DO_NOTHING, db_column='id_tipo', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nome, self.area)

    class Meta:
        db_table = "trabalho"
        managed = True
