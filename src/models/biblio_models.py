from peewee import *

database = SqliteDatabase('biblioteca.db')

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    email = CharField(column_name='EMAIL', null=True)
    id = AutoField(column_name='ID', null=True)
    nome = CharField(column_name='NOME', null=True)
    telefone = CharField(column_name='TELEFONE', null=True)

    class Meta:
        table_name = 'USUARIO'

class Publicacao(BaseModel):
    ano = CharField(column_name='ANO', null=True)
    autor = CharField(column_name='AUTOR', null=True)
    id = AutoField(column_name='ID', null=True)
    nome = CharField(column_name='NOME', null=True)
    tema = CharField(column_name='TEMA', null=True)

    class Meta:
        table_name = 'PUBLICACAO'

class Emprestimo(BaseModel):
    data_devolucao = DateTimeField(column_name='DATA_DEVOLUCAO', null=True)
    data_emprestimo = DateTimeField(column_name='DATA_EMPRESTIMO', null=True)
    id_publicacao = ForeignKeyField(column_name='ID_PUBLICACAO', field='id', model=Publicacao, null=True)
    id_usuario = ForeignKeyField(column_name='ID_USUARIO', field='id', model=Usuario, null=True)
    status = CharField(column_name='STATUS', null=True)

    class Meta:
        table_name = 'EMPRESTIMO'
        primary_key = False



