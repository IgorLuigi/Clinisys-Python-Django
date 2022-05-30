import cProfile
from django.db import models

ESTADOS = [
    ('AC',	'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceara'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondonia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),

]


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices=ESTADOS)

    def __str__(self):
        return "{}  ({})".format(self.nome, self.estado)

class User(models.Model):
    username = models.CharField()
    email = models.CharField()
    password = models.CharField()

class Paciente(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Qual o seu nome?", help_text="Digite seu nome completo")
    nascimento = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(max_length=50)
    cpf = models.IntegerField(verbose_name="Qual o seu CPF?", help_text="Informe o seu CPF")
    rg = models.IntegerField(verbose_name="Qual o seu RG?", help_text="Informe o seu RG")
    endereco = models.CharField(verbose_name="Qual o seu endereço completo?", help_text="Informe o seu endereço completo, contendo RUA, NÚMERO e BAIRRO")

    cidade = models.ForeignKey(Cidade, on_delete = models.PROTECT)

    def __str__(self):
        return "{} + {} + {} + {}".format(self.nome_completo, self.cpf, self.email, self.cidade)

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Qual o seu nome?", help_text="Digite seu nome completo")
    nascimento = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(max_length=50)
    cpf = models.IntegerField(verbose_name="Qual o seu CPF?", help_text="Informe o seu CPF")
    rg = models.IntegerField(verbose_name="Qual o seu RG?", help_text="Informe o seu RG")
    endereco = models.CharField(verbose_name="Qual o seu endereço completo?", help_text="Informe o seu endereço completo, contendo RUA, NÚMERO e BAIRRO")
    funcao = models.CharField(max_length=50, verbose_name="Qual a sua função?", help_text="Informe qual o seu cargo dentro da clínica")

    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return "{} + {} + {} + {}".format(self.nome_completo, self.cpf, self.email, self.cidade)

class Agenda(models.Model):
    data = models.DateField(verbose_name="Data da consulta")
    horario = models.DateTimeField(verbose_name="Horário do atendimento")
    descricaoAtendimento = models.CharField(verbose_name="Descrição do atendimento")

    def __str__(self):
        return "{} + {}".format(self.data, self.horario)

class Consulta(models.Model):
    descricaoConsulta = models.CharField(verbose_name="Descrição da consulta")
    receita = models.CharField(verbose_name="Descrição da receita")
    procedimentoRealizado = models.CharField(verbose_name="Descrição dos procedimentos realizados")

    def __str__(self):
        return "{}".format(self.procedimentoRealizado)

    







# Create your models here.
